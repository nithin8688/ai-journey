from fastapi import FastAPI, HTTPException, Depends 
from fastapi.middleware.cors import CORSMiddleware 
from sqlalchemy.orm import Session 
from typing import List 

from database import SessionLocal, engine 
from models import Base 
from schemas import StudentCreate, StudentResponse 
from crud import add_student, get_all_students, get_student_by_id, update_student_marks, delete_student

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student API with PostgreSQL")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal() 
    try:
        yield db 
    finally: 
        db.close() 


@app.post("/students", response_model=StudentResponse, status_code=201)
async def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    if student.marks < 0 or student.marks > 100:
        raise HTTPException(status_code=404, detail="Marks must between 0 to 100")
    return add_student(db, student)
    

@app.get("/students", response_model=List[StudentResponse])
async def get_students(db: Session = Depends(get_db)):
    return get_all_students(db)

@app.get("/students/topper", response_model=StudentResponse)
async def get_topper(db: Session = Depends(get_db)):
    students = get_all_students(db)
    if not students: 
        raise HTTPException(status_code=404, detail="No student found")
    return max(students, key=lambda x:x.marks)

@app.get("/students/{student_id}", response_model=StudentResponse)
async def get_student(student_id: int, db: Session = Depends(get_db)):
    student = get_student_by_id(db, student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="404 student not found")
    return student 

@app.put("/students/{student_id}", response_model=StudentResponse)
async def update_student(student_id: int, new_marks: int, db: Session = Depends(get_db)):
    if new_marks < 0 or new_marks > 100:
        raise HTTPException(status_code=400, detail="marks must be 0 to 100")
    updated = update_student_marks(db, student_id, new_marks) 
    if updated is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated 


@app.delete("/students/{student_id}", response_model=StudentResponse)
async def remove_student(student_id: int, db: Session = Depends(get_db)):
    delete = delete_student(db, student_id) 
    if delete is None:
        raise HTTPException(status_code=404, detail="student not found")
    return delete

@app.get("/students/search", response_model=List[StudentResponse])
async def search_students(
    name: str = None,
    subject: str = None,
    db: Session = Depends(get_db)
):
    query = db.query(Student)
    if name:
        query = query.filter(Student.name.ilike(f"%{name}%"))
    if subject:
        query = query.filter(Student.subject.ilike(f"%{subject}"))
    return query.all()