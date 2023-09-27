#!/usr/bin/python3
"""square"""
class Square:
    def __init__(self, size=0):
        """init"""
        self.size = size
    @property
    def size(self):
        """size"""
        return self.__size
    @size.setter
    def size(self, v):
        """size"""
        if not isinstance(v, int):
            raise TypeError("size must be an integer")
        if v < 0:
            raise ValueError("size must be >= 0")
        self.__size = v
    def area(self):
        """area"""
        return self.__size ** 2
