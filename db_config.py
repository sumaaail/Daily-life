import sqlite3
from flask import g
from flask import Flask

# location of database
DATABASE = 'database.db'

# instantiation flask object
app = Flask(__name__)


def get_db():
    db = getattr(g, '_database', None)
    print(db)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db
