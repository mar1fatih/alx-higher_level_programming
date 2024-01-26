#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""


if __name__ == "__main__":
    import urllib.parse
    import urllib.request
    from sys import argv

    url = argv[1]
    email = argv[2]
    data = urllib.parse.urlencode({"email": email})
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
