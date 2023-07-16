#!/usr/bin/python3
"""Defines class Rectangle that inherits from Base"""
from base import Base


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
