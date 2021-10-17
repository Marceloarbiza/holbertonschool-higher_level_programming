#!/usr/bin/python3
"""
==========================
Creation of the base class
==========================
"""

import json


class Base:
    """ base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ init the base class """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps([d for d in list_dictionaries])

    @classmethod
    def save_to_file(cls, list_objs):
        """  writes the JSON string representation of list_objs to a file """

        if list_objs is not None:
            list_objs = [i.to_dictionary() for i in list_objs]

        filename = cls.__name__ + '.json'
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """

        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            dummy = Rectangle(3, 5)
        elif cls is Square:
            dummy = Square(3)
        else:
            dummy = None

        dummy.update(**dictionary)

        return dummy
