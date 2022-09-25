#!/usr/bin/python3
"""A sxript that fetches an url using urllib
using request and prints X-content-Id"""

import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
