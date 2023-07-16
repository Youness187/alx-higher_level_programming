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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        with open((cls.__name__ + ".json"), "w") as jsonFile:
            if list_objs is None:
                jsonFile.write("[]")
            else:
                list_dictionaries = [obj.to_dictionary() for obj in list_objs]
                jsonFile.write(Base.to_json_string(list_dictionaries))
