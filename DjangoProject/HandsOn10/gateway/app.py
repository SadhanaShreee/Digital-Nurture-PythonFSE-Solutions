from flask import Flask, request, Response
import requests

app = Flask(__name__)

COURSE_SERVICE_URL = 'http://127.0.0.1:5001'
STUDENT_SERVICE_URL = 'http://127.0.0.1:5002'


@app.route('/api/courses/', methods=['GET', 'POST'])
def proxy_courses_root():
    return forward_request(f'{COURSE_SERVICE_URL}/api/courses/')


@app.route('/api/courses/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy_courses(path):
    return forward_request(f'{COURSE_SERVICE_URL}/api/courses/{path}')


@app.route('/api/students/', methods=['GET', 'POST'])
def proxy_students_root():
    return forward_request(f'{STUDENT_SERVICE_URL}/api/students/')


@app.route('/api/students/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy_students(path):
    return forward_request(f'{STUDENT_SERVICE_URL}/api/students/{path}')


def forward_request(target_url):
    try:
        resp = requests.request(
            method=request.method,
            url=target_url,
            json=request.get_json(silent=True),
            params=request.args,
            timeout=5
        )
    except requests.exceptions.ConnectionError:
        return {'error': 'Service unavailable'}, 503

    return Response(resp.content, status=resp.status_code, content_type=resp.headers.get('Content-Type'))


if __name__ == '__main__':
    app.run(port=5000, debug=True)