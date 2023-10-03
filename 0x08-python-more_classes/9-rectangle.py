#!/usr/bin/python3
"""
Rectangle class
"""


class Rectangle:
    """rectangle"""

    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """__init__ of the Rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """property for width(self)"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) is not (int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if type(value) is not (int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area"""
        area = self.__height * self.__width
        return area

    def perimeter(self):
        """returns rectangle perimeter"""
        if self.__height == 0:
            return 0
        if self.__width == 0:
            return 0
        perimeter = self.__height + self.__height + (self.__width * 2)
        return perimeter

    def __str__(self):
        """print the rectangle with the character #"""
        if self.__height == 0 or self.__width == 0:
            string = ""
            return string
        rows = []
        for i in range(self.__height):
            row = str(Rectangle.print_symbol) * self.__width
            rows.append(row)
        string = "\n".join(rows)
        return string

    def __repr__(self):
        """return a string representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """print deletion of the rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size"""
        return cls(size, size)
