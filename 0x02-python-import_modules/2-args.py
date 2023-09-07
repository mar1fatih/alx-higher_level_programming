#!/usr/bin/python3

if __name__ != "__main__":
    exit()
import sys

c = len(sys.argv)
c -= 1
if c == 0:
    print("0 arguments.")
elif c == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(c))
for j in range(c):
    print("{}: {}".format(i + 1, sys.argv[i + 1]))
