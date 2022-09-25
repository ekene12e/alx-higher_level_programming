#!/usr/bin/python3
import requests


if __name__ == '__main__':
    result = requests.get('https://api.github.com/user', auth=('ekene12e', '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'))
    my_id = result.json()['id']
    print(my_id)