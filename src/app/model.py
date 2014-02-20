from app import app, db

class TodoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(240), unique=True)

    def __init__(self, description):
        self.description = description

    def __repr__(self):
        return '<TODO %r>' % self.description
