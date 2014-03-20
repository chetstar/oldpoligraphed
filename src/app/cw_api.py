from apikey import _API_KEY
import requests
import json
from date_convert import javascript_timestamp
import datetime

def cw_search_keywords(keywords, date_low, date_high, granularity):
    API_KEY = _API_KEY
    api_results = []
    for keyword in keywords:
        query_params = {'apikey': API_KEY,
                    'phrase': keyword,
                    'start_date': date_low,
                    'end_date': date_high,
                    'granularity': granularity
                    }

        endpoint = 'http://capitolwords.org/api/dates.json'

        response = requests.get(endpoint, params=query_params)
        if response.status_code == 200:
            results = json.loads(response.text)
            results_entire_range = add_all_days('2014-01-01', '2014-02-28', results)
            for result in results_entire_range['results']:
                result['day'] = javascript_timestamp(result['day'])
            api_results.append(results)

    return api_results

def add_all_days(start_date, end_date, result):

    '''Function is used to add days with no results back into the list of results
       so that the graph will plot a point of 0 for that day.'''

    date_low = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    date_high = datetime.datetime.strptime(end_date, '%Y-%m-%d')

    returned_dates = []
    for i in result['results']:
       returned_dates.append(datetime.datetime.strptime(i['day'], '%Y-%m-%d'))

    for i in range((date_high - date_low).days + 1):
        date =  date_low + datetime.timedelta(i)
        date_string = date.strftime('%Y-%m-%d')
        if date not in returned_dates:
            no_result = {"count": 0,
                                "percentage": 0,
                                "total": 0,
                                "day": date_string,
                                "raw_count": 0
                                }
            result['results'].insert(i, no_result)

    return result
