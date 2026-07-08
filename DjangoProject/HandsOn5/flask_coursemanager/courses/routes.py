# task 1
"""
from flask import Blueprint, jsonify, request

courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses')

@courses_bp.route('/', methods=['GET'])
def get_courses():
    return jsonify([])

@courses_bp.route('/', methods=['POST'])
def create_course():
    data = request.get_json()
    return jsonify(data), 201

"""
"""
# handson5 task 1
from flask import Blueprint, jsonify, request

courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses')

courses_data = []   # temporary storage — acts like a fake database for now


def make_response_json(data, status_code):
    return jsonify({'status': 'success', 'data': data}), status_code


@courses_bp.route('/', methods=['GET'])
def get_courses():
    return make_response_json(courses_data, 200)


@courses_bp.route('/', methods=['POST'])
def create_course():
    data = request.get_json()

    if not data or 'name' not in data or 'code' not in data or 'credits' not in data:
        return jsonify({'status': 'error', 'message': 'name, code, and credits are required'}), 400

    data['id'] = len(courses_data) + 1
    courses_data.append(data)
    return make_response_json(data, 201)


@courses_bp.route('/<int:course_id>/', methods=['GET'])
def get_course(course_id):
    for course in courses_data:
        if course['id'] == course_id:
            return make_response_json(course, 200)
    return jsonify({'status': 'error', 'message': 'Course not found'}), 404


@courses_bp.route('/<int:course_id>/', methods=['PUT'])
def update_course(course_id):
    for course in courses_data:
        if course['id'] == course_id:
            course.update(request.get_json())
            return make_response_json(course, 200)
    return jsonify({'status': 'error', 'message': 'Course not found'}), 404


@courses_bp.route('/<int:course_id>/', methods=['DELETE'])
def delete_course(course_id):
    for course in courses_data:
        if course['id'] == course_id:
            courses_data.remove(course)
            return make_response_json(None, 200)
    return jsonify({'status': 'error', 'message': 'Course not found'}), 404

"""

# handson5 task 2   
from flask import Blueprint, jsonify, request
from extensions import db   # ← changed from "from app import db"
from courses.models import Course

courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses')


def make_response_json(data, status_code):
    return jsonify({'status': 'success', 'data': data}), status_code


@courses_bp.route('/', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    result = [c.to_dict() for c in courses]
    return make_response_json(result, 200)


@courses_bp.route('/', methods=['POST'])
def create_course():
    data = request.get_json()

    if not data or 'name' not in data or 'code' not in data or 'credits' not in data:
        return jsonify({'status': 'error', 'message': 'name, code, and credits are required'}), 400

    course = Course(
        name=data['name'],
        code=data['code'],
        credits=data['credits'],
        department_id=data.get('department_id')
    )
    db.session.add(course)
    db.session.commit()
    return make_response_json(course.to_dict(), 201)


@courses_bp.route('/<int:course_id>/', methods=['GET'])
def get_course(course_id):
    course = Course.query.get_or_404(course_id)
    return make_response_json(course.to_dict(), 200)


@courses_bp.route('/<int:course_id>/', methods=['PUT'])
def update_course(course_id):
    course = Course.query.get_or_404(course_id)
    data = request.get_json()

    if 'name' in data:
        course.name = data['name']
    if 'code' in data:
        course.code = data['code']
    if 'credits' in data:
        course.credits = data['credits']

    db.session.commit()
    return make_response_json(course.to_dict(), 200)


@courses_bp.route('/<int:course_id>/', methods=['DELETE'])
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    return make_response_json(None, 200)


@courses_bp.route('/<int:course_id>/students/', methods=['GET'])
def get_course_students(course_id):
    course = Course.query.get_or_404(course_id)
    students = [e.student.to_dict() for e in course.enrollments]
    return make_response_json(students, 200)
