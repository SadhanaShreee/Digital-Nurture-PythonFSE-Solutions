from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    code = Column(String, unique=True)
    credits = Column(Integer)
    department_id = Column(Integer, ForeignKey('departments.id'))