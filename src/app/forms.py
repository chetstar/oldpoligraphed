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

from app.models import User

class EditForm(Form):
    nickname = TextField('nickname', validators = [Required()])

    def __init__(self, original_nickname, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.original_nickname = original_nickname

    def validate(self):
        if not Form.validate(self):
            return False
        if self.nickname.data == self.original_nickname:
            return True
        user = User.query.filter_by(nickname = self.nickname.data).first()
        if user != None:
            self.nickname.errors.append('This nickname is already in use. Please choose another one.')
            return False
        return True