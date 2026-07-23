from flask import Flask, jsonify, request

app = Flask(__name__)

courses_data = [
    {'id': 1, 'name': 'Data Structures', 'code': 'CS101', 'credits': 4}
]

@app.route('/api/courses/<int:course_id>/', methods=['GET'])
def get_course(course_id):
    course = next((c for c in courses_data if c['id'] == course_id), None)
    if course is None:
        return jsonify({'error': 'Course not found'}), 404
    return jsonify(course)

@app.route('/api/courses/', methods=['GET'])
def get_courses():
    return jsonify(courses_data)

if __name__ == '__main__':
    app.run(port=5001, debug=True)