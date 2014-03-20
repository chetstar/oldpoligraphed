import requests
import pprint
from src.apikey import _API_KEY

API_KEY = _API_KEY

query_params = { 'apikey': API_KEY,
                 'phrase': 'fiscal cliff' 
               }

endpoint = 'http://capitolwords.org/api/text.json'

response = requests.get( endpoint, params=query_params)
data = response.json

pprint.pprint(data)