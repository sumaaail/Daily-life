from flask import Blueprint,request,Response,jsonify,render_template,make_response
from api.api import *
students = Blueprint('students', __name__)


@students.route('/')
def index():
    print(request.headers.get('REMOTE_ADDR'))
    print(request.headers.get('HTTP_X_FORWARDED_FOR'))
    print(request.remote_addr)
    print(request.environ.get('REMOTE_ADDR'))
    print(request.environ.get('HTTP_X_FORWARDED_FOR'))
    r = render_template('students.html')
    response = make_response(r, 200)
    return response


@students.route("/list")
def list():
    data = demo_select('cmd')
    return data


@students.route("/all")
def all():
    data = select_all('students')
    return data


@students.route('/readme')
def readme():
    return "jinbao mama ai ni"