#!/usr/bin/python3
"""
    - Makes a request to a library and displays value of a header
"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    header_value = requests.get(url)
    print(header_value.headers.get('X-Request-Id'))
