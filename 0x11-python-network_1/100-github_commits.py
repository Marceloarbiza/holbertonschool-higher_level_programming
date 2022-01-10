#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
"""

from requests import get
from sys import argv

if __name__ == "__main__":
    init = "https://api.github.com/repos/{}/{}/commits"\
            .format(argv[2], argv[1])
    r_g = get(init)
    commits = r_g.json()

    try:
        for count in range(10):
            print("{}: {}".format(commits[count]
                  .get("sha"), commits[count].get("commit")
                  .get("author").get("name")))

    except IndexError:
        pass
