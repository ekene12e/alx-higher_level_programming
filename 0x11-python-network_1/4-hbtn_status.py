#!/usr/bin/python3
"""A sxript that fetches an url using urllib
using request library"""

import requests


if __name__ == '__main__':
    result = requests.get('https://alx-intranet.hbtn.io/status')
    print(f'Body response:')
    print(f'\t- type: {type(result.text)}')
    print(f'\t- content: {result.text}')
