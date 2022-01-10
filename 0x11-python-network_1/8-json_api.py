#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
"""

import requests
from requests import get
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    req = get(url)
    datax = {}
    if sys.argv[1] is None:
        datax['q'] = ""
    else:
        datax['q'] = letter
    res = post(url, data=datax)

    try:
        res_json = res.json()
        if res_json['id'] and res_json['name']:
            print('[{}] {}'.format(res_json['id'], res_json['name']))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
