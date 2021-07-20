
from db_config import *
from handler.students import students
from handler.user import user
from handler.news import news
from handler.fav import fav

app.register_blueprint(students, url_prefix='/students')
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(news, url_prefix='/news')
app.register_blueprint(fav, url_prefix='/fav')


# @app.route('/')
# def index():
#     # data = []
#     # cur = get_db().cursor()
#     # for row in cur.execute("SELECT * from students"):
#     #     data.append(row)
#     return "welcome to jin bao de home"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port='5000', debug=True)
