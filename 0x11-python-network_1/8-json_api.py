#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
"""

import requests
from requests import post
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    datax = {}
    args = sys.argv
    if len(args) > 1:
        datax['q'] = args[1]
    res = post(url, data=datax)

    try:
        res_json = res.json()
        if res_json.get('id') and res_json.get('name'):
            print('[{}] {}'.format(res_json.get('id'), res_json.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
