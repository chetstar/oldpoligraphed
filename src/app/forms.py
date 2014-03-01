from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, SubmitField, IntegerField
from wtforms.validators import Required

class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)
    submit = SubmitField('Login')

class SavedGraphForm(Form):
    graph_name = TextField('Graph Name', validators=[Required()])
    keyword_1 = TextField('Keyword 1', validators=[Required()])
    keyword_2 = TextField('Keyword 2', validators=[Required()])
    submit = SubmitField('Save Graph!')

class DeleteGraph(Form):
    graph_id = IntegerField('')
    submit = SubmitField('Delete')

class KeywordSearchForm(Form):
    keyword_1 = TextField('Keyword 1', validators=[Required()])
    keyword_2 = TextField('Keyword 2', validators=[Required()])
    submit = SubmitField('Graph!')
