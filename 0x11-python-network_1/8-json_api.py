#!/usr/bin/python3
"""
    - Takes in a letter and sends a POST request
    - to a url with letter as parameter
"""


if __name__ == "__main__":
    import requests
    import sys

    url = 'http://0.0.0.0:5000/search_user'
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {'q': letter}
    response = requests.post(url, payload)
    try:
        json_res = response.json()
        if json_res == {}:
            print("No result")
        else:
            print("[{}] {}".format(json_res.get("id"), json_res.get("name")))
    except ValueError:
        print("Not a valid JSON")
