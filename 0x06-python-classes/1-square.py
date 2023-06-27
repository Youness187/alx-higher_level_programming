#!/usr/bin/python3
"""Square Class.

This module contains an empty class that defines a square.

Usage Example:

    Square = __import__('0-square').Square

    my_square = Square()
    print(type(my_square))
    print(my_square.__dict__)
"""
class Square:
    """Defines the blueprint of a square.

    Attribute:
        size: An integer indicating the size of the square object.
    """

    def __init__(self, size):
        """An object constructor method.

        Initiatilizes Square with size.

        Arg:
            size: A integer representing object size
        """
        self.__size = size