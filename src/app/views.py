from app import app, db, lm, oid
from apikey import _API_KEY
import requests
import json
from forms import LoginForm, SavedGraphForm, KeywordSearchForm, DeleteGraph
from models import User, ROLE_USER, ROLE_ADMIN, SavedGraph
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required

@app.route('/graph', methods=['GET', 'POST'])
@login_required
def graph():
    user = g.user
    form_keywords = None
    saved_graphs = None
    api_results = None
    deleted_graph_id = None
    deleted_graph = None
    API_KEY = _API_KEY
    keyword_form = KeywordSearchForm(prefix="keyword_form")
    saved_graph_form = SavedGraphForm(prefix="saved_graph_form")
    saved_graphs_query = SavedGraph.query.filter_by(user_id = user.id)
    if saved_graphs_query:
        saved_graphs = saved_graphs_query
    delete_graph_form = DeleteGraph(prefix="delete_graph_form")

    #If the keyword form is submitted

    if keyword_form.validate_on_submit() and keyword_form.submit.data:

        form_keywords = [
            keyword_form.keyword_1.data,
            keyword_form.keyword_2.data]

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
        return render_template('graph.html', saved_graphs=saved_graphs, graph=api_results, user=user, keyword_form=keyword_form, saved_graph_form=saved_graph_form, delete_graph_form = delete_graph_form )

    if saved_graph_form.validate_on_submit() and saved_graph_form.submit.data:
        save_graph = SavedGraph(
            graph_name = saved_graph_form.graph_name.data,
            keyword_1 = saved_graph_form.keyword_1.data,
            keyword_2 = saved_graph_form.keyword_2.data,
            user_id = user.id
            )
        db.session.add(save_graph)
        db.session.commit()
        return redirect(url_for('graph'))

    if delete_graph_form.validate_on_submit() and delete_graph_form.submit.data:
        deleted_graph_id = delete_graph_form.graph_id.data
        deleted_graph = db.session.query(SavedGraph).filter_by(id=deleted_graph_id).first()
        db.session.delete(deleted_graph)
        db.session.commit()
        return redirect(url_for('graph'))

    return render_template('graph.html', saved_graphs=saved_graphs, graph=api_results, user=user, keyword_form=keyword_form, saved_graph_form=saved_graph_form, delete_graph_form = delete_graph_form )
    # return redirect(url_for('test_save_graph'))

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
        nickname = User.make_unique_nickname(nickname)
        user = User(nickname=nickname, email=resp.email, role=ROLE_USER)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember=remember_me)
    return redirect(request.args.get('next') or url_for('index'))

@app.route('/edit', methods = ['GET', 'POST'])
@login_required
def edit():
    form = EditForm(g.user.nickname)