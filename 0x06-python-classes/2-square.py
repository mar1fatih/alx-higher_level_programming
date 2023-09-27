#!/usr/bin/python3
"""square"""
class Square:
    """square"""
    def __init__(self, size=0):
        """init"""
        if size < 0:
            raise ValueError("size must be >= 0")
        if isinstance(size, int) == None:
            raise TypeError("size must be an integer")
        self.__size = size
