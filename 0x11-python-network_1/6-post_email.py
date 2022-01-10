#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
"""

import sys
from requests import post


if __name__ == "__main__":
    url = sys.argv[1]
    value = post(url, data={'email': sys.argv[2]})
    print(value.text)
