#!/usr/bin/python3
'''
    -Sends a request to a url
    - managees urllib errors
'''


if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    url = sys.argv[1]
    try:
        response = urllib.request.urlopen(url)
        data = response.read().decode('utf-8')
        print(data)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
