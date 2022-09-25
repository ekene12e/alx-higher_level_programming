#!/usr/bin/python3
"""Takes in a url and print
a content of the header"""
from urllib.request import Request, urlopen
from urllib.error import URLError
import sys


if __name__ == '__main__':
    req = Request(sys.argv[1])
    try:
        with urlopen(req) as res:
            print(res.read().decode('utf-8'))
    except URLError as e:
        if hasattr(e, 'code'):
            print(f'Error code: {e.code}')
