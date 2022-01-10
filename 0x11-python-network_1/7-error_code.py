#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
"""

import requests
from requests import get
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = get(url)
    status = req.status_code
    if status >= 400:
        print('Error code: {}'.format(status))
    else:
        print(status)
