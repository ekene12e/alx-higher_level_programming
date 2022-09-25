#!/usr/bin/python3
"""Takes in a github username and
password and prints the userId"""

import requests
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    result = requests.get('https://api.github.com/user',
                          auth=(username, password))
    my_id = result.json().get('id')
    print(my_id)
