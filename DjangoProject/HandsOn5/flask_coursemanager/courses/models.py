from extensions import db 

class Department(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    hod = db.Column(db.String(100))
    budget = db.Column(db.Numeric(10,2))

    courses = db.relationship('Course',back_populates='department')

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(10), unique=True, nullable=False)
    credits = db.Column(db.Integer)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))

    department = db.relationship('Department', back_populates='courses') # task 1

    def to_dict(self): # added for task 2
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'credits': self.credits,
            'department_id': self.department_id
        }


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    enrollment_year = db.Column(db.Integer)

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'department_id': self.department_id,
            'enrollment_year': self.enrollment_year
        }


class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    enrollment_date = db.Column(db.Date)
    grade = db.Column(db.String(2), nullable=True)
    student = db.relationship('Student', backref='enrollments') # task 2
    course = db.relationship('Course', backref='enrollments')