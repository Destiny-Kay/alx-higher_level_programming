#!/usr/bin/python3
"""
    - A fetches data from a url
"""


if __name__ == "__main__":
    import requests

    res = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(res.text.__class__))
    print('\t- content: {}'.format(res.text))
