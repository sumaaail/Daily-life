from api.api import *
from flask import Blueprint, request, Response, render_template, make_response,jsonify

fav = Blueprint('fav', __name__)


@fav.route('/')
def fav_index():
    data = select_all('fav')
    return jsonify(data)


@fav.route('/savefav',methods=['GET'])
def savefav():
    uid = select_id_by_uname(request.form['uname'])
    fav = request.form['fav']
    values = [uid,fav]
    state = insert_fav(values)
    if state:
        return "fav added successfully"
    return "error occurs when adding fav"


@fav.route('/fetchfav',methods=['GET'])
def fetchfav():
    # uid = select_id_by_uname(request.form['uname'])
    uid = select_id_by_uname('sumail')
    data = select_fav_by_uid(uid[0][0])
    return jsonify(data)

