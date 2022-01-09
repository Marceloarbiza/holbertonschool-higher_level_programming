#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
"""

import urllib.request
import sys
import urllib.parse
from urllib.error import HTTPError


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as r:
            read_r = r.read()
            read_r = read_r.decode('utf-8')
            print(read_r)
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
