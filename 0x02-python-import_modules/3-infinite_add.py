#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    i = 0
    c = len(argv) - 1
    for j in range(c):
        i += int(argv[j + 1])
    print(i)
