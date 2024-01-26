#!/usr/bin/python3
"""sends POST request to the URL passed with the email as a parameter"""


if __name__ == '__main__':
    from sys import argv
    import requests

    url = argv[1]
    email = argv[2]
    req = requests.post(url, {"email": email})
    print(req.text)
