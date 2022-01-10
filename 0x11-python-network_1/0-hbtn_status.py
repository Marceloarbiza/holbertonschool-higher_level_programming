#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
"""
import urllib.request
import sys


def fetcher():
    """ fetch """    
    url = "https://intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as req:
        r = req.read()
        print("Body response:")
        print("\t- type: {}".format(type(r)))
        print("\t- content: {}".format(r))
        print("\t- utf8 content: {}".format(r.decode('utf8')))

if __name__ == "__main__":
    fetcher()
