#!/usr/bin/python3
"""A sxript that fetches an url using urllib"""

import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as r:
        res = r.read()
    print(f'Body respose:')
    print(f'\t- type: {type(res)}')
    print(f'\t- content: {res}')
    print(f"\t- utf8 content: {res.decode('utf8')}")
