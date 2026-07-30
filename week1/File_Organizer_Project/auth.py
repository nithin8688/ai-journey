from fastapi import Depends, HTTPException 
from fastapi.security import OAuth2PasswordBearer 
from jose import JWTError, jwt 
from passlib.context import CryptContext 
from pydantic import BaseModel 
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os 


load_dotenv()
# CONFIG 
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 

# SETUP 
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# FAKE USER DB 
fake_users_db = {
    "nithin": {
        "username": "nithin",
        "hashed_password": pwd_context.hash("secret123"),
        "role": "admin",
    }
}

# MODELS 
class Token(BaseModel):
    access_token: str 
    token_type: str 

# HELPER FUNCTIONS
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password) 

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

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