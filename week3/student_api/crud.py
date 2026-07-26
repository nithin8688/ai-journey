from sqlalchemy.orm import Session 
from models import Student
from schemas import StudentCreate 

def add_student(db: Session, student_data: StudentCreate):
    student = Student(
        name=student_data.name,
        marks=student_data.marks,
        subject=student_data.subject,
        passed=student_data.marks >= 75
    )
    db.add(student)
    db.commit()
    db.refresh(student)
    return student 

def get_all_students(db: Session):
    return db.query(Student).all()

def get_student_by_id(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first() 

def update_student_marks(db: Session, student_id: int, new_marks: int):
    student = db.query(Student).filter(Student.id == student_id).first() 
    if student is None:
        return None 
    student.marks = new_marks 
    student.passed = new_marks >= 75 
    db.commit()
    db.refresh(student)
    return student 

def delete_student(db: Session, student_id: int):
    student = db.query(Student).filter(Student.id == student_id).first() 
    if student is None:
        return None 
    db.delete(student)
    db.commit() 
    return student 
