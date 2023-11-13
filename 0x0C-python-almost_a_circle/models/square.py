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

    def update(self, *args, **kwargs):
        """update square attribute"""
        if args:
            self.upargs(args)
        else:
            self.upkwargs(kwargs)

    def upargs(self, args):
        """called when *args giving"""
        for i in range(len(args)):
            if i == 0:
                self.id = args[0]
            if i == 1:
                self.size = args[1]
            if i == 2:
                self.x = args[2]
            if i == 3:
                self.y = args[3]

    def upkwargs(self, kwargs):
        """called when **kwargs giving"""
        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            if key == "size":
                self.size = value
            if key == "x":
                self.x = value
            if key == "y":
                self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
