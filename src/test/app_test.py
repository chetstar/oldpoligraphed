import unittest
import app.model
from app.apikey import _API_KEY
from app.config import API_KEY

class TestApp(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_apikey(self):
        expected = API_KEY
        actual = _API_KEY

        self.assertEquals(expected, actual, "apikey don't match: %s | %s"
            % (expected, actual))
