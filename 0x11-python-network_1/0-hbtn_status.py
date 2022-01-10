#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
"""
from urllib.request import urlopen
import sys


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    with urlopen(url) as req:
        r = req.read()
        print("Body response:")
        print("\t- type: {}".format(type(r)))
        print("\t- content: {}".format(r))
        print("\t- utf8 content: {}".format(r.decode('utf8')))
