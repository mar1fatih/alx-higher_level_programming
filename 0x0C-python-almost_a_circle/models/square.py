#!/usr/bin/python3
"""square form rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str"""
        return "[{}] ({}) {}/{} - {}".\
               format(type(self).__name__, self.id, self.x, self.y,
                      self.height)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __upargs(self, *args):
        if args[0] is not None:
            self.id = args[0]
        if args[1] is not None:
            self.size = args[1]
        if args[2] is not None:
            self.x = args[2]
        if args[3] is not None:
            self.y = args[3]

    def __upkwargs(self, id=None, size=None, x=None, y=None):
        if id is not None:
            self.id = id
        if width is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """update"""
        if args:
            self.__upargs(*args)
        elif kwargs:
            self.__upkwargs(**kwargs)

    def to_dictionary(self):
        """square dictionary"""
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
