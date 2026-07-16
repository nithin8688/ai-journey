###### Day 10 - Async FastAPI + Middleware + Error Handling ######
# Sync endpoint - blocks the server during the sleep
from fastapi import FastAPI, HTTPException, Request, Depends 
from fastapi.middleware.cors import CORSMiddleware 
import time 
import asyncio 
from pydantic import BaseModel
from fastapi.responses import JSONResponse 

app = FastAPI()
student_db = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def timing_middleware(request: Request, call_next):
    start = time.time()
    print(f"Incoming: {request.method} {request.url.path}")

    response = await call_next(request)

    duration = time.time() - start 
    response.headers["X-Process-Time"] = str(duration)
    print(f"Completed in {duration:.3f}s")

    return response 


# Handle any unhandled exception globally
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc:Exception):
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal sever error",
            "detail": str(exc),
            "path": str(request.url.path),
        }
    )
#Handle 404s globally
@app.exception_handler(404)
async def not_found(request: Request, exc):
    return JSONResponse(
        status_code=404,
        content={
            "error": "Route not found",
            "path": str(request.url.path)
        }
    )

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

def validate_marks(marks: int):
    if marks < 0 or marks > 100:
        raise HTTPException(status_code=400, detail="Invalid marks")
    return marks 

def verify_student_exists(student_id: int):
    for student in student_db:
        if student["id"] == student_id:
            return student 
    raise HTTPException(status_code=404, detail="Student not found")

@app.get("/slow")
def slow_function():
    time.sleep(3)
    return {"Done": True}

@app.get("/fast")
async def fast_endpoint():
    await asyncio.sleep(3)
    return {"done": True}

@app.post("/students", response_model=StudentResponse, status_code=201)
async def create_student(student: Student):
    if student.marks < 0 or student.marks > 100:
        raise HTTPException(status_code=400, detail="Marks must be between 0 to 100")
    
    new_student = {
        "id": len(student_db) + 1,
        "name": student.name,
        "marks": student.marks,
        "subject": student.subject,
        "passed": student.marks >= 75, 
    }
    student_db.append(new_student)
    return new_student 

@app.get("/students", response_model=list[StudentResponse])
async def get_students():
    return student_db

@app.get("/students/{student_id}")
async def get_student(student_id: int):
    await asyncio.sleep(0)
    for s in student_db:
        if s["id"] == student_id:
            return s 
    raise HTTPException(status_code=404, detail="Not found") 
    

@app.get("/check-marks/{marks}")
async def check_marks(marks: int, validated: int= Depends(validate_marks)):
    await asyncio.sleep(0)
    return {"marks": validated, "valid": True}

@app.get("/Verify_student_exist/{student_id}")
async def verify_student_exist(student_id: int, student =Depends(verify_student_exists)):
    return {"student_id":student, "valid":True}

