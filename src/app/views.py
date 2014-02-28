from app import app, db, lm, oid
from apikey import _API_KEY
import requests
import json
from forms import LoginForm
from models import User, ROLE_USER, ROLE_ADMIN, SavedGraph
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required


@app.route('/add', methods=['POST'])
def save_graph():
    user_id = 999
    #replace with functioning user ID
    if request.form['graph_name'] and request.form['keyword_1'] and request.form['keyword_2']:
        save_graph = SavedGraph(
            user_id=user_id,
            graph_name=request.form['graph_name'],
            keyword_1=request.form['keyword_1'],
            keyword_2=request.form['keyword_2'])
        db.session.add(save_graph)
        db.session.commit()
        return redirect(url_for('graph'))
    return "Must complete all form fields."


@app.route('/submit_graph', methods=['POST'])
def submit_graph():
    API_KEY = _API_KEY
    form_keywords = [
        request.form['graph_keyword_1'],
        request.form['graph_keyword_2']]

    api_results = {}
    for keyword in form_keywords:
        query_params = {'apikey': API_KEY,
                        'phrase': keyword,
                        'start_date': '2014-01-06',
                        'end_date': '2014-01-11',
                        'granularity': 'day'
                        }

        endpoint = 'http://capitolwords.org/api/dates.json'

        response = requests.get(endpoint, params=query_params)
        json_data = json.loads(response.text)

        keyword_results = []
        for item in json_data['results']:
            keyword_results.append({item['day']: item['count']})

        api_results[keyword] = keyword_results

    saved_graphs = SavedGraph.query.all()
    return render_template('graph.html', saved_graphs=saved_graphs, graph=api_results)


@app.route('/delete_graph', methods=['POST'])
def delete_graph():
    deleted_graph_id = request.form['deleted_graph_id']
    # deleted_graph_id = 1
    deleted_graph = db.session.query(SavedGraph).filter_by(id=deleted_graph_id).first()
    db.session.delete(deleted_graph)
    db.session.commit()
    return redirect(url_for('graph'))


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
    return render_template('index.html', user=user)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/jobs')
def jobs():
    return render_template('jobs.html')


@app.route('/donations')
def donations():
    return render_template('donations.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html', title='Sign In', form=form, providers=app.config['OPENID_PROVIDERS'])


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.before_request
def before_request():
    g.user = current_user


@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email, role=ROLE_USER)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember=remember_me)
    return redirect(request.args.get('next') or url_for('index'))


@app.route('/graph')
def graph():
    saved_graphs = SavedGraph.query.all()
    return render_template('graph.html', saved_graphs=saved_graphs)
