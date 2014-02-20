from app import app, db
#from forms import LoginForm
#from models import User, ROLE_USER, ROLE_ADMIN
from flask import render_template, redirect, url_for
from flask import request
from model import TodoItem
#from flask.ext.login import login_user, logout_user, current_user, login_required
#from flask import render_template, flash, redirect, session, url_for, request, g



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
    return render_template('base.html', todos=todo_list)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/dataInput')
def dataInput():
    return "dataInput!"
