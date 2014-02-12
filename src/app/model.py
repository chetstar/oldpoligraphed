import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db') 
db = SQLAlchemy(app)

class TodoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(240), unique=True)

    def __init__(self, description):
        self.description = description

    def __repr__(self):
        return '<TODO %r>' % self.description
