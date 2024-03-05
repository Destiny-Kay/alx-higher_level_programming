#!/usr/bin/python3
'''
    -Sends a request to a url
    - managees urllib errors
'''


if __name__ == "__main__":
    from urllib import request, error
    import sys

    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            data = response.read().decode('UTF-8')
            print(data)
    except error.HTTPError as e:
        print("Error code:", e.code)
