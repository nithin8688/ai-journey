from sqlalchemy.orm import Session 
from week3.student_api.database import SessionLocal
from week3.student_api.models import Student 

def add_student(db: Session, name: str, marks:int, subject: str):
    student = Student(
        name=name,
        marks=marks,
        subject=subject,
        passed=marks>=75
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
    student.passed = new_marks>=75
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

db = SessionLocal() 

s1 = add_student(db, "Ali", 88, "Math")
s2 = add_student(db, "Sara", 95, "Physics")
s3 = add_student(db, "Bilal", 60, "AI")
print("Added:", s1.name, s1.id)

all_student = get_all_students(db)
for s in all_student:
    print(f"{s.id}: {s.name} - {s.marks}")

student = get_student_by_id(db, s1.id)
print("Found:", student.name)

updated = update_student_marks(db,s3.id,80)
print("Updated:", updated.name, updated.marks, updated.passed) 

deleted = delete_student(db, s2.id)
print("Deleted:", deleted.name)

db.close()