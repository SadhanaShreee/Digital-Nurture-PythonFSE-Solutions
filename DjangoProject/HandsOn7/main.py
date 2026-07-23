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

from fastapi import FastAPI, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Optional

from database import engine, Base, get_db
from models import Course as CourseModel, Department as DepartmentModel, Student as StudentModel, Enrollment as EnrollmentModel
from schemas import CourseCreate, CourseResponse, StudentCreate, StudentResponse, EnrollmentCreate

app = FastAPI(
    title='Course Management API',
    description='API for managing departments, courses, students, and enrollments',
    version='1.0',
    contact={'name': 'Sadhana', 'email': 'your_email@example.com'}
)


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get('/')
def root():
    return {'message': 'API running'}


#  DEPARTMENTS 

@app.post('/api/departments/', tags=['Departments'])
async def create_department(name: str, db: AsyncSession = Depends(get_db)):
    dept = DepartmentModel(name=name)
    db.add(dept)
    await db.commit()
    await db.refresh(dept)
    return dept


# COURSES

@app.post(
    '/api/courses/',
    response_model=CourseResponse,
    status_code=201,
    tags=['Courses'],
    summary='Create a new course',
    response_description='The newly created course'
)
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


@app.get('/api/courses/', response_model=list[CourseResponse], tags=['Courses'])
async def get_courses(skip: int = 0, limit: int = 10, department_id: Optional[int] = None, db: AsyncSession = Depends(get_db)):
    query = select(CourseModel).offset(skip).limit(limit)
    if department_id is not None:
        query = query.where(CourseModel.department_id == department_id)
    result = await db.execute(query)
    return result.scalars().all()


@app.get('/api/courses/{course_id}', response_model=CourseResponse, tags=['Courses'])
async def get_course(course_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(CourseModel).where(CourseModel.id == course_id))
    db_course = result.scalar_one_or_none()
    if db_course is None:
        raise HTTPException(status_code=404, detail='Course not found')
    return db_course


@app.put('/api/courses/{course_id}', response_model=CourseResponse, tags=['Courses'])
async def update_course(course_id: int, course: CourseCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(CourseModel).where(CourseModel.id == course_id))
    db_course = result.scalar_one_or_none()

    if db_course is None:
        raise HTTPException(status_code=404, detail='Course not found')

    for key, value in course.dict().items():
        setattr(db_course, key, value)

    await db.commit()
    await db.refresh(db_course)
    return db_course


@app.delete('/api/courses/{course_id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Courses'])
async def delete_course(course_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(CourseModel).where(CourseModel.id == course_id))
    db_course = result.scalar_one_or_none()

    if db_course is None:
        raise HTTPException(status_code=404, detail='Course not found')

    await db.delete(db_course)
    await db.commit()


@app.get('/api/courses/{course_id}/students/', response_model=list[StudentResponse], tags=['Courses'])
async def get_course_students(course_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(StudentModel)
        .join(EnrollmentModel, EnrollmentModel.student_id == StudentModel.id)
        .where(EnrollmentModel.course_id == course_id)
    )
    return result.scalars().all()


# STUDENTS

@app.post('/api/students/', response_model=StudentResponse, status_code=201, tags=['Students'])
async def create_student(student: StudentCreate, db: AsyncSession = Depends(get_db)):
    new_student = StudentModel(**student.dict())
    db.add(new_student)
    await db.commit()
    await db.refresh(new_student)
    return new_student


@app.get('/api/students/', response_model=list[StudentResponse], tags=['Students'])
async def get_students(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(StudentModel))
    return result.scalars().all()


@app.get('/api/students/{student_id}', response_model=StudentResponse, tags=['Students'])
async def get_student(student_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(StudentModel).where(StudentModel.id == student_id))
    student = result.scalar_one_or_none()
    if student is None:
        raise HTTPException(status_code=404, detail='Student not found')
    return student


@app.delete('/api/students/{student_id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Students'])
async def delete_student(student_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(StudentModel).where(StudentModel.id == student_id))
    student = result.scalar_one_or_none()
    if student is None:
        raise HTTPException(status_code=404, detail='Student not found')
    await db.delete(student)
    await db.commit()


# ENROLLMENTS

def send_confirmation_email(student_email: str):
    print(f'Sending confirmation to {student_email}')


@app.post('/api/enrollments/', status_code=201, tags=['Enrollments'])
async def create_enrollment(enrollment: EnrollmentCreate, background_tasks: BackgroundTasks, db: AsyncSession = Depends(get_db)):
    new_enrollment = EnrollmentModel(
        student_id=enrollment.student_id,
        course_id=enrollment.course_id
    )
    db.add(new_enrollment)
    await db.commit()
    await db.refresh(new_enrollment)

    background_tasks.add_task(send_confirmation_email, enrollment.student_email)

    return {'id': new_enrollment.id, 'message': 'Enrollment created'}