"""
from fastapi import FastAPI
from schemas import CourseCreate
app = FastAPI(title='Course Management API', version='1.0')

@app.get('/')
def root():
    return {'message': 'API running'}

@app.post('/api/courses/') # task 1 for post method
async def create_course(course: CourseCreate):
    return {'received': course}

@app.get('/api/courses/{course_id}')
async def get_course(course_id: int):
    return {'course_id': course_id}

from typing import Optional

@app.get('/api/courses/')
async def get_courses(skip: int = 0, limit: int = 10, department_id: Optional[int] = None):
    return {'skip': skip, 'limit': limit, 'department_id': department_id}

"""

# task 2 for database integration
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Optional

from database import engine, Base, get_db
from models import Course as CourseModel
from schemas import CourseCreate

app = FastAPI(title='Course Management API', version='1.0')

# detailed implementation of the startup event to create tables in the database

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get('/')
def root():
    return {'message': 'API running'}


@app.post('/api/courses/')
async def create_course(course: CourseCreate, db: AsyncSession = Depends(get_db)):
    new_course = CourseModel(
        name=course.name,
        code=course.code,
        credits=course.credits,
        department_id=course.department_id
    )
    db.add(new_course)
    await db.commit()
    await db.refresh(new_course)
    return new_course

from models import Department as DepartmentModel

@app.post('/api/departments/')
async def create_department(name: str, db: AsyncSession = Depends(get_db)):
    dept = DepartmentModel(name=name)
    db.add(dept)
    await db.commit()
    await db.refresh(dept)
    return dept


@app.get('/api/courses/{course_id}')
async def get_course(course_id: int):
    return {'course_id': course_id}



@app.get('/api/courses/')
async def get_courses(skip: int = 0, limit: int = 10, department_id: Optional[int] = None, db: AsyncSession = Depends(get_db)):
    query = select(CourseModel).offset(skip).limit(limit)
    if department_id is not None:
        query = query.where(CourseModel.department_id == department_id)
    result = await db.execute(query)
    courses = result.scalars().all()
    return courses