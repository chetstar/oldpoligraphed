from app import db

ROLE_USER = 0
ROLE_ADMIN = 1


class SavedGraph(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    graph_name = db.Column(db.String(240))
    keyword_1 = db.Column(db.String(240))
    keyword_2 = db.Column(db.String(240))

    def __init__(self, graph_name, keyword_1, keyword_2):
        self.graph_name = graph_name
        self.keyword_1 = keyword_1
        self.keyword_2 = keyword_2

    def __repr__(self):
        return '<Graph %r>' % self.id


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(120), unique=True)
    role = db.Column(db.SmallInteger, default=ROLE_USER)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.nickname)
