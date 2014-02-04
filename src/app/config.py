#variables for ingestion by flask app
from src.app.apikey import _API_KEY

API_KEY = _API_KEY

class _DefaultSettings(object):
    USERNAME = 'world'
    SECRET_KEY = 'development key'
    DEBUG = True
    

