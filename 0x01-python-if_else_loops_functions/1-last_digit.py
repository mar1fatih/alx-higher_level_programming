#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    modi = number % 10
if number < 0:
    modi = number % -10
if number == 0:
    modi = number
print(f"Last digit of {number:d} is {modi:d} and is", end=" ")
if modi > 5:
    print("greater than 5")
elif modi == 0:
    print("0")
else:
    print("less than 6 and not 0")
