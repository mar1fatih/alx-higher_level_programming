#!/usr/bin/python3
"""square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """constrator"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representing class atribute"""
        return "[Square] ({}) {}/{} - {}".\
               format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.validation("width", value)
        self.width = value
        self.height = value
