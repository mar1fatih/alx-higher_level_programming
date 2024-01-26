#!/usr/bin/python3
"""python script to request from url"""
from urllib.request import Request, urlopen


if __name__ == "__main__":
    request = Request("https://alx-intranet.hbtn.io/status")
    with urlopen(request) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode("utf-8")))
