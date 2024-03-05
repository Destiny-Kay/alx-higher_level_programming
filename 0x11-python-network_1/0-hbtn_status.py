#!/usr/bin/python3
'''fetches a url resource'''

if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        data = res.read()
        print('Body response:')
        print(f'\t- type: {type(data)}')
        print(f'\t- content: {data}')
        print('\t- utf8 content: {}'.format(data.decode('utf-8')))
