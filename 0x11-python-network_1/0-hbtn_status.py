#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
"""
from urllib import request


if __name__ == "__main__":
    with request.urlopen("https://intranet.hbtn.io/status") as req:
        r = req.read()
        print("Body response:")
        print("\t- type: {}".format(type(r)))
        print("\t- content: {}".format(r))
        print("\t- utf8 content: {}".format(r.decode('utf8')))
