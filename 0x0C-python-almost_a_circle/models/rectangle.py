#!/usr/bin/python3
"""Defines class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Represent the Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get the width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of Rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get the height of Rectangle"""
        return self.__heigth

    @height.setter
    def height(self, value):
        """set the height of Rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__heigth = value

    @property
    def x(self):
        """get the x of Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """set the x of Rectangle"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get the y of Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the y of Rectangle"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """get the area of Rectangle"""
        return self.width * self.height

    def display(self):
        """print the Rectangle"""
        [print() for y in range(self.y)]
        for col in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            for row in range(self.width):
                print("#", end="")
            print()

    def update(self, *args):
        """update the Rectangle"""
        if len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    if args[i] is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]

    def __str__(self):
        """Returns the str() repesentation of the Rectangle"""
        string = "[Rectangle] ({}) {}/{} - {}/{}"
        return string.format(self.id, self.x, self.y, self.width, self.height)
