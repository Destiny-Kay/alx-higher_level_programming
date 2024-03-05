#!/usr/bin/python3
"""
    - A fetches data from a url
"""


if __name__ == "__main__":
    import requests

    res = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body respone:')
    print('\t- type: {}'.format(type(res.text)))
    print('\t- content: {}'.format(res.text))
