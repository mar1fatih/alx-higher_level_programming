#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response,
if greater or equal 400 print error message with status code"""


if __name__ == '__main__':
    from sys import argv
    import requests

    url = argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print('Error code: {}'.format(response.status_code))
    else:
        print(response.text)
