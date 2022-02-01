#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
"""


from requests import get
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = get(url)
    value = r.headers.get('X-Request-Id')
    print(value)
