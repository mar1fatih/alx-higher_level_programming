#!/usr/bin/python3
"""read file"""


def read_file(filename=""):
    """read_file"""
    with open(filename, "r")as file:
        print(file.read())
