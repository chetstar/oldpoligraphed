from app import app, db, lm, oid
from forms import LoginForm
from model import User, ROLE_USER, ROLE_ADMIN, SavedGraph
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required


@app.route('/add', methods=['POST'])
def save_graph():
    if request.form['graph_name'] and request.form['keyword_1'] and request.form['keyword_2']:
        save_graph = SavedGraph(
            graph_name=request.form['graph_name'],
            keyword_1=request.form['keyword_1'],
            keyword_2=request.form['keyword_2'])
        db.session.add(save_graph)
        db.session.commit()
        return redirect(url_for('test_save_graph'))
    return "Must complete all form fields."


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
    return render_template('base.html', user=user)


@app.route('/about')
def about():
    return render_template('about.html')


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


@app.route('/testSaveGraph')
def test_save_graph():
    saved_graphs = SavedGraph.query.all()
    return render_template('testSaveGraph.html', saved_graphs=saved_graphs)
