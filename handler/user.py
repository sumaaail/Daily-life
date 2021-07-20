

from api.api import *
from flask import Blueprint, request, Response, render_template, make_response,jsonify

user = Blueprint('user', __name__)

@user.route('/')
def user_index():
    data = select_all('user')
    return jsonify(data)


# registered: return 0; wrong pwd: return 1
@user.route('/login',methods=['POST'])
def check_user():
    uname = request.form['uname']
    pwd = select_pwd_by_uname(uname)
    if not pwd:
        return "not registed"
    else:
        if pwd[0][0] != request.form['pwd']:
            return "wrong password"
        else:
            return "login successfully"


@user.route('/register',methods=['POST'])
def register():
    uname = request.form['uname']
    pwd = request.form['pwd']
    phone = request.form['phone']
    if uname in [node[0] for node in select_uname(uname)]:
        return "name already registed"
    values = [uname,pwd,phone]
    state = register(values)
    if state:
        return "register successfully"
    return "error occurs when registration"


@user.route('/delete',methods=['GET'])
def delete_account():
    state = delete_account_by_uname(request.form['uname'])
    if state:
        return "deleted account successfully"
    return "error occurs when deleting"
