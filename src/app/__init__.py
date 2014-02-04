# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, redirect, url_for
from model import db, TodoItem

# from src.app.config import API_KEY

# create the application
app = Flask(__name__)
# app.config.from_object(_DefaultSettings)
app.config.from_pyfile("config.py", silent = True)
# del _DefaultSettings


def init_db():
    """Create the database tables."""
    db.create_all()

@app.route('/add', methods=['POST'])
def add_todo():
    if 'todo_item' in request.form:
        todo = TodoItem(description = request.form['todo_item'])
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('index'))
    return "Unknown Error"

@app.route('/')
def index():
    todo_list = TodoItem.query.all()
    return render_template('hello.html', todos=todo_list)