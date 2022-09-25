#!/usr/bin/python3
"""Takes in a url and prints 
a content of the header"""
import urllib.request
import sys


if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as res:
        info_id = res.info()['X-Request-Id']
        print(info_id)
