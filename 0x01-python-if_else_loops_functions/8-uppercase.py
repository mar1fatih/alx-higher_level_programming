#!/usr/bin/python3
def islower(d):
    if ord(d) >= 97 and ord(d) <= 123:
        return True
    else:
        return False


def uppercase(str):
    for d in str:
        print("{:c}".format(ord(d)) if islower(d) else ord(d) - 32, end="")
    print("")
