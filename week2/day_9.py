###### FastAPI: Routes, Pydantic, Request/Response ######
#### Part 1 - Your first FastAPI app ####
'''from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Journey API is running. Okay"}

@app.get("/hello/{name}")
def greet(name: str):
    return {"greeting": f"Hello, {name}"}

#### Part 2 - the decorator is a route #### 
# @app.get("/students")
# @app.post("/students")
# @app.put("/students/{id}")
# @app.delete("/students/{id}")    
    
#### Part 3 - path parameters ####    
@app.get("/student_id/{student_id}")
def get_student(student_id: int):
    return {"student_id": student_id, "name": f"Student_{student_id}"}

#### Part 4 - query parameters ####
@app.get("/students")
def get_students(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit, "message": f"Returning {limit} students"}

#### Part 5 - Pydantic models (request body) ####
from pydantic import BaseModel  

class Student(BaseModel):
    name: str 
    marks: int 
    subject: str 
@app.post("/Nithin/")
def thin_details(student: Student):
    return { 
        "message": f"Student_{student.name} oiuytrdfghj",
        "data": student  
    }'''

#### Part 6 - response models and status codes #### 
'''from fastapi import FastAPI, HTTPException 
from pydantic import BaseModel
from typing import List 

app = FastAPI() 

# In-memory "database" for now 
student_db = [] 

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
def create_Student(student: Student):
    if student.marks < 0 or student.marks > 100:
        raise HTTPException(status_code=400, detail="Marks must be between 0 and 100")
    
    new_student = {
         "id": len(student_db) + 1,
         "name": student.name, 
         "marks": student.marks,
         "subject": student.subject, 
         "passed": student.marks >= 75 
    }
    student_db.append(new_student)
    return new_student 

@app.get("/students", response_model=List[StudentResponse])
def get_all_students():
    return student_db 

@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int):
    for s in student_db:
        if s["id"] == student_id:
            return s 
    raise HTTPException(status_code=404, detail=f"Student {student_id} not found")'''


# 1. student request means: what all student details are required for the student API would call, then based on that API student would give the response

# 2. i will create the In memory student database with empty list


from fastapi import FastAPI, HTTPException, Request, Depends
from pydantic import BaseModel 
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse 
import time 
import asyncio 

app = FastAPI() 
students_db = []

class Student(BaseModel):
    name: str
    marks : int 
    subject: str

class StudentResponse(BaseModel):
    id: int 
    name: str
    marks: int 
    subject: str 
    passed: bool 

@app.post("/students", response_model=StudentResponse, status_code=201)
async def create_student(student: Student):
    if student.marks < 0 or student.marks > 100:
        raise HTTPException(status_code=400, detail="Marks should between 0 to 100")
    
    new_student = {
        "id": len(students_db) + 1,
        "name": student.name,
        "marks": student.marks, 
        "subject": student.subject,
        "passed": student.marks >= 75
    }
    students_db.append(new_student)
    return new_student

@app.get("/students", response_model=list[StudentResponse])
async def all_students():
    return students_db

@app.get("/students/topper", response_model=StudentResponse)
async def get_topper():
    if not students_db:
        raise HTTPException(status_code=404, detail=f"404 no student found")
    return max(students_db, key=lambda x:x["marks"])

@app.get("/students/{student_id}", response_model=StudentResponse)
async def get_student_id(student_id: int):
    for s in students_db:
        if s["id"] == student_id:
            return s 
    raise HTTPException(status_code=404, detail=f"404 student_id:{student_id} not found")

@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    for student in students_db:
        if student["id"] == student_id:
            students_db.remove(student)
            return student
    raise HTTPException(status_code=404, detail=f"404 student_id:{student_id} not found")




'''{
    "name": "Nithin",
    "marks": 90,
    "subject": "GenAI"
  }
  {
    "name": "Vinod",
    "marks": 95,
    "subject": "Mech"
  }
  {
    "name": "Sai",
    "marks": 88,
    "subject": "Inter"
  }
  {
    "name": "Vinay",
    "marks": 85,
    "subject": "EEE"
  }
  {
    "name": "Vardhan",
    "marks": 75,
    "subject": "AI"
  }'''