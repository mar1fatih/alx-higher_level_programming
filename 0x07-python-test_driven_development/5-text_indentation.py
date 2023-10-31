#!/usr/bin/python3
"""
text_indentation
"""


def text_indentation(text):
    """adding 2 new lines after '.?:'"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    delims = [".", "?", ":"]
    for i in delims:
        text = (i + "\n\n").join([ln.strip(" ") for ln in text.split(i)])
    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
