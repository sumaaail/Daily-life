from api.api import *
from flask import Blueprint, request, Response, render_template, make_response,jsonify

news = Blueprint('news',__name__)

@news.route('/')
def index():
    data = select_all('news')
    return jsonify(data)
