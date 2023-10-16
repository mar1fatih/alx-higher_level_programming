#!/usr/bin/python3
"""rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self.vlidate("width", value)
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        self.vlidate("height", value)
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        self.vlidate("x", value)
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        self.vlidate("y", value)
        self.__y = value

    def validate(self, name, value):
        """validating values"""
        if type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if name == "height" or name == "width":
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        elif value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def def area(self):
        """area calc"""
        return self.width * self.height

    def display(self):
        """display"""
        print_dis = ("\n" * self.y) + \
                    ((" " * self.x) + "#" * self.width + "\n") * self.height
        print(print_dis, end="")

    def __str__(self):
        """str"""
        return "{} ({}) {}/{} - {}/{}".\
            format(type(self).__name__, self.id, self.x,
                   self.y, self.width, self.height)

    def __upargs(self, *args):
        """__upargs"""
        if args[0] is not None:
            self.id = args[0]
        if args[1] is not None:
            self.width = args[1]
        if args[2] is not None:
            self.height = args[2]
        if args[3] is not None:
            self.x = args[3]
        if args[4] is not None:
            self.y = args[4]

    def __upkwargs(self, id=None, width=None, height=None, x=None, y=None):
        """__upkwargs"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
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
        """dictionary"""
        return {"id": self.id, "width": self.__width,
                "height": self.__height, "x": self.__x, "y": self.__y}
