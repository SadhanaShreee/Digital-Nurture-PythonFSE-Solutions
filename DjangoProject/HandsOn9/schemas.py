from pydantic import BaseModel
from typing import Optional, List


class CourseCreate(BaseModel):
    name: str
    code: str
    credits: int
    department_id: int


class CourseUpdate(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    credits: Optional[int] = None
    department_id: Optional[int] = None


class CourseResponse(BaseModel):
    id: int
    name: str
    code: str
    credits: int
    department_id: int

    class Config:
        from_attributes = True
    

class DepartmentResponse(BaseModel):
    id: int
    name: str
    courses: List[CourseResponse] = [] # nested schema where all courses can be listed while returning 
                                       # the department details
                                       
class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    department_id: int


class StudentResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    department_id: int


class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int
    student_email: str  # used only to trigger the background email task

class UserCreate(BaseModel):
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str