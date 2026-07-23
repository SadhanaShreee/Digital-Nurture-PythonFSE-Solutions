from sqlalchemy.orm import sessionmaker
from models import engine, Department, Student, Course, Enrollment

Session = sessionmaker(bind=engine)
session = Session()

# Step 81: insert departments and students
dept_cs = Department(dept_name='Computer Science')
dept_math = Department(dept_name='Mathematics')
dept_phy = Department(dept_name='Physics')
session.add_all([dept_cs, dept_math, dept_phy])
session.commit()   # commit now so dept_cs.dept_id gets populated

students = [
    Student(first_name='Asha', last_name='Rao', email='asha@example.com', enrollment_year=2022, dept_id=dept_cs.dept_id),
    Student(first_name='Ben', last_name='Kumar', email='ben@example.com', enrollment_year=2022, dept_id=dept_cs.dept_id),
    Student(first_name='Chitra', last_name='Iyer', email='chitra@example.com', enrollment_year=2021, dept_id=dept_math.dept_id),
    Student(first_name='Dev', last_name='Nair', email='dev@example.com', enrollment_year=2022, dept_id=dept_cs.dept_id),
    Student(first_name='Esha', last_name='Menon', email='esha@example.com', enrollment_year=2023, dept_id=dept_phy.dept_id),
]
session.add_all(students)
session.commit()

# Step 82: courses and enrollments
courses = [
    Course(course_code='CS101', course_name='Intro to Programming'),
    Course(course_code='CS102', course_name='Data Structures'),
    Course(course_code='MA101', course_name='Calculus I'),
]
session.add_all(courses)
session.commit()

enrollments = [
    Enrollment(student_id=students[0].student_id, course_id=courses[0].course_id),
    Enrollment(student_id=students[1].student_id, course_id=courses[0].course_id),
    Enrollment(student_id=students[2].student_id, course_id=courses[2].course_id),
    Enrollment(student_id=students[3].student_id, course_id=courses[1].course_id),
]
session.add_all(enrollments)
session.commit()


cs_students = session.query(Student).join(Department).filter(Department.dept_name == 'Computer Science').all()
for s in cs_students:
    print(s.first_name, s.last_name)



# TASK 3
from sqlalchemy.orm import joinedload

query_count_before = query_count  # reset marker

eager_enrollments = session.query(Enrollment).options(
    joinedload(Enrollment.student),
    joinedload(Enrollment.course)
).all()

for e in eager_enrollments:
    print(e.student.first_name, '-', e.course.course_name)   # NO extra queries now — already loaded

print(f"Queries issued with joinedload: {query_count - query_count_before}")

