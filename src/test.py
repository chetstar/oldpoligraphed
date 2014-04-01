
#!flask/bin/python
import os
# import sys
# topdir = os.path.join(os.path.dirname(__file__), "..")
# sys.path.append(topdir)
import unittest
import requests
import pprint
print os.getcwd()
from apikey import _API_KEY
from config import API_KEY
from config import basedir
from app import app, db
from app.models import User
# import app.cw_api


class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_make_unique_nickname(self):
        u = User(nickname = 'john', email = 'john@example.com')
        db.session.add(u)
        db.session.commit()
        nickname = User.make_unique_nickname('john')
        assert nickname != 'john'
        u = User(nickname = nickname, email = 'susan@example.com')
        db.session.add(u)
        db.session.commit()
        nickname2 = User.make_unique_nickname('john')
        assert nickname2 != 'john'
        assert nickname2 != nickname

    def test_API_KEY(self):
        API_KEY = _API_KEY
        query_params = { 'apikey': API_KEY,
                         'phrase': 'fiscal cliff' 
                       }
        endpoint = 'http://capitolwords.org/api/text.json'
        response = requests.get( endpoint, params=query_params)
        data = response.json
        pprint.pprint(data)

    def test_apikey(self):
        expected = API_KEY
        actual = _API_KEY

        self.assertEquals(expected, actual, "apikey don't match: %s | %s"
            % (expected, actual))


if __name__ == '__main__':
    unittest.main()