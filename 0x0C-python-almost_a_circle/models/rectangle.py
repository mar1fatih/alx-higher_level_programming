#!/usr/bin/python3
"""rectangle module"""
from models.base import Base


class Rectangle(Base):
    """class rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """constractor"""
        self.validation("width", width)
        self.validation("height", height)
        self.validation("x", x)
        self.validation("y", y)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self.validation("width", value)
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        self.validation("height", value)
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        self.validation("x", value)
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        self.validation("y", value)
        self.__y = value

    def validation(self, name, value):
        """validate the attribute values"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if name == "height" or name == "width":
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        elif name == "x" or name == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """calculate the area"""
        return self.__width * self.__height

    def display(self):
        """display the rectangle with #"""
        print("".join("\n" for y in range(self.__y)) +
              "\n".join("".join(" " * self.__x +
                        "#" * self.__width) for j in range(self.__height)))

    def __str__(self):
        """string representing class"""
        return "[Rectangle] ({}) {}/{} - {}/{}".\
               format(self.id, self.__x, self.__y, self.__width, self.__height)

    def updatev1(self, args):
        """called when *args giving"""
        for i in range(len(args)):
            if i == 0:
                self.id = args[0]
            if i == 1:
                self.__width = args[1]
            if i == 2:
                self.__height = args[2]
            if i == 3:
                self.__x = args[3]
            if i == 4:
                self.__y = args[4]

    def updatev2(self, kwargs):
        """called when **kwargs giving"""
        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            if key == "width":
                self.__width = value
            if key == "height":
                self.__height = value
            if key == "x":
                self.__x = value
            if key == "y":
                self.__y = value

    def update(self, *args, **kwargs):
        """update the attribute giving"""
        if args:
            self.updatev1(args)
        else:
            self.updatev2(kwargs)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {'x': self.__x, 'y': self.__y, 'id': self.id,
                'height': self.__height, 'width': self.__width}
