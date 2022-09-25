#!/usr/bin/python3
"""Takes in a github username and
repo name and prints the last10 commits"""

import requests
import sys


if __name__ == '__main__':
    a = sys.argv[1]
    b = sys.argv[2]
    r = requests.get(f'https://api.github.com/repos/{b}/{a}/commits')
    commits = r.json()
    try:
        for i in range(10):
            print(f"{commits[i]['sha']}: {commits[i]['commit']['author']['name']}")
    except IndexError:
        pass
