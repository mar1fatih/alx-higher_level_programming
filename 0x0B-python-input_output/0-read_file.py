#!/usr/bin/python3
"""read file"""


def read_file(filename=""):
    """read_file"""
    with open(filename, encoding="UTF8")as file:
        print(file.read(), end="")
