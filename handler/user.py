

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
    data_rcv = request.data
    data2str = str(data_rcv,encoding="utf-8")
    dic = eval(data2str)
    uname = dic['username']
    pwd = select_pwd_by_uname(uname)
    if not pwd:
        return "2"    # cannot find uname in database
    else:
        if pwd[0][0] != dic['password']:
            return "1"    # wrong pwd
        else:
            return "0"    # login successfully


@user.route('/register',methods=['POST'])
def register():
    data_rcv = request.data
    data2str = str(data_rcv, encoding="utf-8")
    dic = eval(data2str)
    uname = dic['username']
    pwd = dic['password']
    phone = dic['phone']
    if uname in [node[0] for node in select_uname(uname)]:
        return "2"  # name already registed
    values = [uname,pwd,phone]
    state = user_register(values)
    if state:
        return "0"  # register successfully
    return "1"  # error occurs when registration


@user.route('/delete',methods=['POST'])
def delete_account():
    data_rcv = request.data
    data2str = str(data_rcv, encoding="utf-8")
    dic = eval(data2str)
    state = delete_account_by_uname(dic['uname'])
    if state:
        return "deleted account successfully"
    return "error occurs when deleting"
