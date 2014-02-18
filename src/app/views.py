from app import app, db
from flask import render_template, redirect, url_for
from flask import request
from model import TodoItem

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
    return render_template('index.html', todos=todo_list)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/dataInput')
def dataInput():
    return "dataInput!"

@app.route('/base_html')
def base_html():
    return render_template('basejd.html')