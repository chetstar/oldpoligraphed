# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
import os
from config import basedir

lm = LoginManager()
lm.init_app(app)
# need a tmp folder
oid = OpenID(app, os.path.join(basedir, 'tmp'))

# create the application
app = Flask(__name__)

# app.config.from_object(_DefaultSettings)
app.config.from_pyfile("config", silent = True)
# del _DefaultSettings

db = SQLAlchemy(app)
def init_db():
    """Create the database tables."""
    db.create_all()

Bootstrap(app)

from app import views, model
