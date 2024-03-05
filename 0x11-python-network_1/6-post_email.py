#!/usr/bin/python3
"""
    - Sends a POST request to the passed URL with email parameter
"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    response = requests.post(url, data)
    print(response.text)
