"""
Fetch data from API

Author: Sam Lev
3/16/26
"""
import requests
from datetime import date, timedelta

ONE_DAY = timedelta(1)

def get_data_from_server(endpoint, days):
    data = []
    curr_day = date.today()
    for i in range(days):
        url = build_url(endpoint, curr_day.year, curr_day.month, curr_day.day)
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"API request error code: {response.status_code}")
        data.extend(response.json())
        curr_day -= ONE_DAY
    return data


def build_url(endpoint, year, month, day):
    return f"https://{endpoint}/_cat/indices/*{year}*{month}*{day}?v&h=index,pri.store.size,pri&format=json&bytes=b"