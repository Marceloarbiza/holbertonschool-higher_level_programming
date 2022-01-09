#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
"""

import urllib.request
import sys
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    data = {}
    data['email'] = sys.argv[2]
    url_values = urllib.parse.urlencode(data)
    values_ascii = url_values.encode('ascii')
    req = urllib.request.Request(url, values_ascii)
    with urllib.request.urlopen(req) as r:
        read_r = r.read()
        read_r = read_r.decode('utf-8')
        print(read_r)
