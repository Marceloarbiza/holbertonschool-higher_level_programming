#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
"""

import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    obj = 'X-Request-Id'
    with urllib.request.urlopen(url) as r:
        print(r.headers.get(obj))
