import datetime
import random

from api.api import *
from flask import Blueprint, request, Response, render_template, make_response, jsonify
from collections import deque

news = Blueprint('news', __name__)

words = deque(['资讯'], maxlen=5)


@news.route('/fetch', methods=['GET'])
def fetch():
    print("begin to fetch")
    k_words = [word for word in words]
    print(k_words)
    retData = doSpider(keyword=str(k_words), sortBy='focus')
    print(retData[0])
    return jsonify(retData)


@news.route('/rec', methods=['GET'])
def rec():
    # 可以保留，此功能可以在登录的时候进行用户喜好标签的计算，现在移植到了定时函数上
    # k_words = getKeywords()
    # for word in k_words:
    #     words.append(word)
    # print("keywords: ", words)
    # return "0"
    return "0"


@news.route('/accurate', methods=['POST', 'GET'])
def accurate():
    data_rcv = request.data
    data2str = str(data_rcv, encoding="utf-8")
    dic = eval(data2str)
    print("info: ", dic['info'])
    retData = doSpider(keyword="重庆大学", sortBy='focus')[0]
    print(retData)
    if retData == -1:
        return "-1"
    return jsonify(retData)


def recTag():
    k_words = getKeywords()
    for word in k_words:
        words.append(word)
    print("keywords: ", words)
    return "0"


def changeTag():
    kwords = ['娱乐', '体育', '政治', '经济', '美食']
    words.append(random.sample(kwords, 1)[0])
    print(words, '\n', datetime.now())
