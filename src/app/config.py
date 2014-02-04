#variables for ingestion by flask app

import imp
import os
# from src.app.apikey import _API_KEY

base_path = os.path.dirname(os.path.abspath(__file__))
#import _API_KEY
_path = 'apikey.py'
apikey_path = os.path.normpath(os.path.join(base_path, _path))
apikey = imp.load_source('apikey', apikey_path)

API_KEY = apikey._API_KEY

class _DefaultSettings(object):
    USERNAME = 'world'
    SECRET_KEY = 'development key'
    DEBUG = True
    

