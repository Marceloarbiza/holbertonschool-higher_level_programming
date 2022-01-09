#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    obj = 'X-Request-Id'
    r = requests.get(url)
    value = r.headers[obj]
    print(value)
