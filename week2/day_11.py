from fastapi import FastAPI, Depends, HTTPException, status 
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt 
from passlib.context import CryptContext
from pydantic import BaseModel
from datetime import datetime, timedelta 
from typing import List

# CONFIG
SECRET_KEY = "your-secret-key-keep-this-safe"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# SETUP 
app = FastAPI()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# FAKE USER DB 
fake_users_db = {
    "nithin": {
        "username": "nithin",
        "hashed_password": pwd_context.hash("secret123"),
        "role": "admin"
    },
    "sara": {
        "username": "sara",
        "hashed_password": pwd_context.hash("pass456"),
        "role": "user"
    },
}

class Token(BaseModel):
    access_token: str 
    token_type: str 

class TokenData(BaseModel):
    username: str | None = None 

def verify_password(plain_password, hashed_password):
    return pwd_context.vjerify(plain_password, hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_users_db.get(form_data.username)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password"
        )
    
    if not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password"
        )
    
    token = create_access_token(data={"sub": form_data.username})
    return {"access_token": token, "token_type": "bearer"}

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception 
    except JWTError:
        raise credentials_exception
    
    user = fake_users_db.get(username)
    if user is None:
        raise credentials_exception 
    
    return user

@app.get("/public")
async def public_route():
    return {"message": "Anyone can see this - no token needed"}

@app.get("/protected")
async def protected_route(current_user = Depends(get_current_user)):
    return {
        "message": f"Hello {current_user['username']}",
        "role": current_user["role"]
    }

students_db = []

class Student(BaseModel):
    name: str 
    marks: int 
    subject: str 

class StudentResponse(BaseModel):
    id: int 
    name: str 
    marks: int 
    subject: str 
    passed: bool 

@app.post("/students", response_model=StudentResponse, status_code=201)
async def create_student(student: Student, current_user = Depends(get_current_user)):
    if student.marks < 0 or student.marks > 100:
        raise HTTPException(status_code=400, detail="Marks must between 0 to 100")
    
    new_student = {
        "id": len(students_db)+1,
        "name": student.name,
        "marks": student.marks,
        "subject": student.subject,
        "passed": student.marks >= 75,
    }
    students_db.append(new_student)
    return new_student

@app.get("/students", response_model=List[StudentResponse])
async def get_all_students():
    return students_db