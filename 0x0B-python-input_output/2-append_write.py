#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """append_write"""
    with open(filename, "a", encoding="UTF8") as file:
        file.write(text)
    return len(text)
