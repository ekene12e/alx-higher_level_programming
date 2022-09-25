#!/usr/bin/python3
"""Takes in a url and print
a content of the header"""
from email import message
from urllib.request import Request, urlopen, URLError
import sys


if __name__ == '__main__':
    req = Request(sys.argv[1])
    try:
        with urlopen(sys.argv[1]) as res:
            msg = res.read()
            print(msg.decode('utf-8'))
    except URLError as e:
        if hasattr(e, 'reason'):
            print('Reason: ', e.reason)
        elif hasattr(e, 'code'):
            print('Error code: ', e.code)
