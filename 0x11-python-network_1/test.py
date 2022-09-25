#!/usr/bin/python3
import requests


if __name__ == '__main__':
    result = requests.get('https://alx-intranet.hbtn.io/status')
    print(f'Body response:')
    print(result.headers['X-Request-Id'])