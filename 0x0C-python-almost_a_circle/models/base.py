#!/usr/bin/python3
"""Defines the first class Base"""


class Base:
    """Represent the base class

    Attributes:
        __nb_objects : private class attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
