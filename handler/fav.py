from api.api import *
from flask import Blueprint, request, Response, render_template, make_response, jsonify

fav = Blueprint('fav', __name__)


@fav.route('/savefav', methods=['POST'])
def savefav():
    data_rcv = request.data
    print(data_rcv)
    data2str = str(data_rcv, encoding="utf-8")
    dic = eval(data2str)
    uid = select_id_by_uname(dic['username'])
    fav = dic['sum']
    values = [uid[0][0], fav]
    print("uid: {}, value: {}".format(uid, values))
    state = insert_fav(values)
    if state:
        return "0"  # fav added successfully
    return "1"  # error occurs when adding fav


@fav.route('/fetchfav', methods=['GET', 'POST'])
def fetchfav():
    data_rcv = request.data
    data2str = str(data_rcv, encoding="utf-8")
    dic = eval(data2str)
    uid = select_id_by_uname(dic['username'])
    data = select_fav_by_uid(uid[0][0])
    return jsonify(data)
