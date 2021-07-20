import os.path
import sqlite3
from flask import g
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
# abs location of database
DATABASE = 'database.db'

# instantiation flask object
app = Flask(__name__)
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'base.sqlite')
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# base_db = SQLAlchemy(app)



def get_db():
    db = getattr(g, '_database', None)
    print(db)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

