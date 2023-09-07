#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":

    c = len(argv)
    c -= 1
    if c == 0:
        print("0 arguments.")
    elif c == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(c))
    for j in range(c):
        print("{}: {}".format(j + 1, argv[j + 1]))
