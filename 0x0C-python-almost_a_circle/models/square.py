#!/usr/bin/python3
"""Defines class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent the Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the str() represntation of a Square"""
        string = "[Square] ({}) {}/{} - {}"
        return string.format(self.id, self.x, self.y, self.height)
