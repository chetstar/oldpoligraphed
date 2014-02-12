import unittest
import PyClass_API_Project.src.app.model
from PyClass_API_Project.src.app.apikey import _API_KEY
from PyClass_API_Project.src.app.config import API_KEY

class TestApp(unittest.TestCase):

    def detUp(self):
        pass

    def tearDown(self):
        pass

    def test_apikey(self):
        expected = API_KEY
        actual = _API_KEY

        self.assertEquals(expected, actual, "apikey don't match: %s | %s" 
            % (expected, actual))