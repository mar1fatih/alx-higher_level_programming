#!/usr/bin/python3
"""write on a file"""


def write_file(filename="", text=""):
    """write_file"""
    with open(filename, "w", encoding="UTF8") as file:
        file.write(text)
    return len(text)
