#!/usr/bin/python3
"""
    - Script makes a POST request to a url with some data
    - retunrs the response decoded in utf-8
"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        response_body = response.read()
        print(response_body.decode('utf-8'))
