#!/usr/bin/python3
"""Improve Geometry"""


class BaseGeometry:
    """Geometry"""
    def area(self):
        """area"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """integer_validator"""
        self.name = name
        self.value = value
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
