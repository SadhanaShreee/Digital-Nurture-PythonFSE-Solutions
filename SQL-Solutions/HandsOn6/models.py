from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Numeric
from sqlalchemy.orm import relationship, declarative_base


engine = create_engine("mysql+mysqlconnector://root:Root%40123@localhost/college_db_orm", echo=False)

Base = declarative_base()

# Step 77-78: five model classes with relationships
class Department(Base):
    __tablename__ = 'departments'
    dept_id = Column(Integer, primary_key=True)
    dept_name = Column(String(100), nullable=False)

    students = relationship('Student', back_populates='department')


class Student(Base):
    __tablename__ = 'students'
    student_id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100), unique=True)
    enrollment_year = Column(Integer)
    dept_id = Column(Integer, ForeignKey('departments.dept_id'))

    department = relationship('Department', back_populates='students')
    enrollments = relationship('Enrollment', back_populates='student')


class Professor(Base):
    __tablename__ = 'professors'
    professor_id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    dept_id = Column(Integer, ForeignKey('departments.dept_id'))


class Course(Base):
    __tablename__ = 'courses'
    course_id = Column(Integer, primary_key=True)
    course_code = Column(String(20))
    course_name = Column(String(100))
    professor_id = Column(Integer, ForeignKey('professors.professor_id'))

    enrollments = relationship('Enrollment', back_populates='course')


class Enrollment(Base):
    __tablename__ = 'enrollments'
    enrollment_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.student_id'))
    course_id = Column(Integer, ForeignKey('courses.course_id'))
    grade = Column(String(2), nullable=True)

    student = relationship('Student', back_populates='enrollments')
    course = relationship('Course', back_populates='enrollments')



if __name__ == '__main__':
    Base.metadata.create_all(engine)
    print("Tables created in college_db_orm")