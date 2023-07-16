#!/usr/bin/python3
"""Defines the first class Base"""
import json
import csv


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

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        file_name = str(cls.__name__) + ".json"
        try:
            with open(file_name, "r") as jsonFile:
                list_dictionaries = Base.from_json_string(jsonFile.read())
                return [cls.create(**obj) for obj in list_dictionaries]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes and deserializes in CSV"""
        file_name = cls.__name__ + ".csv"
        with open(file_name, "w", newline="") as csvFile:
            if list_objs is None or list_objs == []:
                csvFile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                write = csv.DictWriter(csvFile, fieldnames=fieldnames)
                for obj in list_objs:
                    write.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """serializes and deserializes in CSV"""
        file_name = cls.__name__ + ".csv"
        try:
            with open(file_name, "r", newline="") as csvFile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvFile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
