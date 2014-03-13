from apikey import _API_KEY
import requests
import json
from date_convert import javascript_timestamp

def cw_search_keywords(keywords):
    API_KEY = _API_KEY
    api_results = []
    for keyword in keywords:
        query_params = {'apikey': API_KEY,
                    'phrase': keyword,
                    'start_date': '2014-01-01',
                    'end_date': '2014-01-31',
                    'granularity': 'day'
                    }

        endpoint = 'http://capitolwords.org/api/dates.json'

        response = requests.get(endpoint, params=query_params)
        if response.status_code == 200:
            results = json.loads(response.text)
            for result in results['results']:
                result['day'] = javascript_timestamp(result['day'])
            api_results.append(results)

    return api_results
