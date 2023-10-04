#!/usr/bin/python3
"""print_square."""


def print_square(size):
    """print a square with #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size >= 0:
        for i in range(size):
            print("#" * size)
    else:
        raise ValueError("size must be >= 0")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
