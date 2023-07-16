#!/usr/bin/python3
"""Defines the first class Base"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
