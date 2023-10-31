#!/usr/bin/python3
"""print square"""


def print_square(size):
    """print square"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
    

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")

