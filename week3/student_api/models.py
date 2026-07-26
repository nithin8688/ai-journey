from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from sqlalchemy.sql import func 
from database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    marks = Column(Integer, nullable=False)
    subject = Column(String(100))
    passed = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    