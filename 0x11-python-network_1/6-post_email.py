#!/usr/bin/python3
"""A script that posts an email as param
to an url"""

import requests
import sys


if __name__ == '__main__':
    payload = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], payload)
    print(r.text)
