from flask import Flask, render_template, Response
from db_config import *
from handler.students import students

app.register_blueprint(students, url_prefix='/students')


@app.route('/')
def index():
    # data = []
    # cur = get_db().cursor()
    # for row in cur.execute("SELECT * from students"):
    #     data.append(row)
    return "welcome to jin bao de home"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port='5000', debug=True)
