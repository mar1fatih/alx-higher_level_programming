#!/usr/bin/python3
"""displays the value of the X-Request-Id"""


if __name__ == "__main__":
    from sys import argv
    from urllib.request import urlopen

    with urlopen(argv[1]) as response:
        print(response.headers["X-Request-Id"])
