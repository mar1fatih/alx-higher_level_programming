#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""


if __name__ == "__main__":
    import urllib.parse
    import urllib.request
    from sys import argv

    url = argv[1]
    email = argv[2]
    value = {'email' : email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
