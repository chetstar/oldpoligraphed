#!flask/bin/python
from app import init_db, app

if __name__ == '__main__':
    init_db()
    app.run()
