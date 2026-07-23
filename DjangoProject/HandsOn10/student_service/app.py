from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

students_data = [
    {'id': 1, 'first_name': 'Sadhana', 'last_name': 'S'}
]
enrollments_data = []

COURSE_SERVICE_URL = 'http://127.0.0.1:5001'


@app.route('/api/students/', methods=['GET'])
def get_students():
    return jsonify(students_data)


@app.route('/api/students/<int:student_id>/enroll', methods=['POST'])
def enroll_student(student_id):
    data = request.get_json()
    course_id = data.get('course_id')

    student = next((s for s in students_data if s['id'] == student_id), None)
    if student is None:
        return jsonify({'error': 'Student not found'}), 404

    try:
        response = requests.get(f'{COURSE_SERVICE_URL}/api/courses/{course_id}/', timeout=3)
    except requests.exceptions.ConnectionError:
        return jsonify({'error': 'Course Service is unavailable'}), 503

    if response.status_code == 404:
        return jsonify({'error': 'Course not found'}), 404

    enrollment = {'student_id': student_id, 'course_id': course_id}
    enrollments_data.append(enrollment)
    return jsonify(enrollment), 201


if __name__ == '__main__':
    app.run(port=5002, debug=True)