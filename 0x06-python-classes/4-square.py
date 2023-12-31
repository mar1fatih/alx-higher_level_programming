#!/usr/bin/python3
"""Square class"""
class Square:
    """code"""
    def __init__(self, size=0):
        """init
            size: size
        """
        self.size = size

    @property
    def size(self):
        """size"""
        return self.__size

    @size.setter
    def size(self, value):
        """size
            value: value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area"""
        return self.__size ** 2
