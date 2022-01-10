#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
"""


from requests import get


if __name__ == "__main__":
    url = get('https://intranet.hbtn.io/status')
    r = get(url)
    print('Body response:')
    print('\t- type: {}'.format(r.text))
    print('\t- content: {}'.format(r.content))
