#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
"""

from requests import get
from requests import post
import sys

if __name__ == "__main__":
    res_json = "https://api.github.com/repos/{}/{}/commits"\
                    .format(sys.argv[2], sys.argv[1])
    res_json = get(res_json)
    res_json = res_json.json()

    try:
        for x in range(10):
            print('{}: {}'.format(res_json[x].get("sha"),
                  res_json[x].get("commit")
                  .get("author").get("name")))
    except IndexError:
        pass
