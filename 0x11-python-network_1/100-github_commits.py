#!/usr/bin/python3
"""Takes in a github username and
repo name and prints the last10 commits"""

import requests
import sys


if __name__ == '__main__':
    a = sys.argv[1]
    b = sys.argv[2]
    r = requests.get(f'https://api.github.com/repos/{b}/{a}/commits')
    count = 1
    while(count <= 10):
        print(r.json()[count]['commit']['tree']['sha'], end='')
        print(f": {r.json()[count]['commit']['author']['name']}")
        count = count + 1
