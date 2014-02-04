import unittest
import imp
import os

test_base_path = os.path.dirname(os.path.abspath(__file__))
#import model
model_path = '../src/app/model.py'
test_model_path = os.path.normpath(os.path.join(test_base_path, model_path))
model = imp.load_source('model', test_model_path)
# import apikey
apikey_path = '../src/app/apikey.py'
test_apikey_path = os.path.normpath(os.path.join(test_base_path, apikey_path))
apikey = imp.load_source('apikey', test_apikey_path)

# expected = model.API_KEY
# actual = apikey._API_KEY

# print expected, actual

class TestApp(unittest.TestCase):

    def detUp(self):
        pass

    def tearDown(self):
        pass

    def test_apikey(self):
        expected = model.API_KEY
        actual = apikey._API_KEY

        self.assertEquals(expected, actual, "apikey don't match: %s | %s" 
            % (expected, actual))