#!/usr/bin/python3
"""Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle"""
    def __init__(self, width, height):
        """__init__"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width

    def area(self):
        """area change"""
        return self.__width + self.__height

    def __str__(self):
        """string"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
