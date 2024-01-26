#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""
import urllib.parse
import urllib.request
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    value = {'email' : email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().encode('utf-8'))
