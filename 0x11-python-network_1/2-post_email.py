#!/usr/bin/python3
"""Takes in a url and email address
then posts the email to the url as data"""
import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    data = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req, data) as res:
        message = res.read()
