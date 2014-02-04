import imp
import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

base_path = os.path.dirname(os.path.abspath(__file__))
#import API_KEY
_path = 'config.py'
config_path = os.path.normpath(os.path.join(base_path, _path))
config = imp.load_source('config', config_path)

API_KEY = config.API_KEY

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class TodoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(240), unique=True)

    def __init__(self, description):
        self.description = description

    def __repr__(self):
        return '<TODO %r>' % self.description
