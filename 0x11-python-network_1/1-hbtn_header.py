#!/usr/bin/python3
'''
    -A script sends requests to a url  using urllib package
    -Gets the headers value for the X-Request-Id
'''


if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers['X-Request-Id'])
