#!/usr/bin/python3
"""square"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size):
        """__init__"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(area):
        """area calc"""
        return self.__size ** 2
