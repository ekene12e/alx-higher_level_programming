#!/usr/bin/python3
"""A script that posts an email as param
to an url"""

import requests
import sys


if __name__ == '__main__':
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print(f'Error code: {r.status_code}')
    else:
        print(r.text)
