from pydantic import BaseModel 
from typing import Optional 

class StudentCreate(BaseModel):
    name: str 
    marks: int
    subject: str 

class StudentResponse(BaseModel):
    id: int
    name: str
    marks: int 
    subject: str 
    passed: bool 

    class Config:
        from_attributes = True 