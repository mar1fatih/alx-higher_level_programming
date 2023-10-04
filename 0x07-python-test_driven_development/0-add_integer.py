#!/usr/bin/python3
"""add_integer method"""


def add_integer(a, b=98):
    """add two intergers
    a: a
    b: b
    Return: int
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    c = int(a) + int(b)
    return c


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
