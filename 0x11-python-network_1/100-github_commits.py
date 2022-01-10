#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
"""

from requests import get
from requests import post
import sys

if __name__ == "__main__":
    res_json = get("https://api.github.com/repos/{}/{}/commits"\
                    .format(argv[2], argv[1])).json()

    try:
        for x in range(10):
            prin('{}: {}'.format(res_json[x].get('sha'),
                  res_json[x].get('commit')
                  .get('authorÂ').get('name')))
    except IndexError:
        pass
