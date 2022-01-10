#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
"""

from requests import get
from requests import post
import sys

if __name__ == "__main__":
    gh_url = "https://api.github.com/user"
    user_ = sys.argv[1]
    pass_ = sys.argv[2]
    res = get(gh_url, auth=(user_, pass_))
    json_res = res.json()
    id_ = json_res.get('id')
    print(id_)
