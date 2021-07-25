from flask_apscheduler import APScheduler
import handler.news
from db_config import *
from handler.user import user
from handler.news import news
from handler.fav import fav

app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(news, url_prefix='/news')
app.register_blueprint(fav, url_prefix='/fav')

scheduler = APScheduler()


class SchedulerConfig(object):
    JOBS = [
        {
            'id': 'changeTag',
            'func': 'handler.news:changeTag',
            'trigger': 'interval',
            'seconds': 5,

        },
        {
            'id': 'recTagFromDB',
            'func': '__main__:recTagFromDB',
            'trigger': 'interval',
            'seconds': 10,
        }
    ]


def recTagFromDB():
    with app.app_context():
        return handler.news.recTag()


app.config.from_object(SchedulerConfig())
if __name__ == '__main__':
    scheduler.init_app(app=app)
    scheduler.start()
    app.run(host="0.0.0.0", port='5000', debug=False)
