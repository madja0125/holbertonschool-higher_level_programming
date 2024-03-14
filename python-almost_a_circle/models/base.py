#!/usr/bin/python3
"""Module with a class called Base"""

import json
from os import path

class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes instances"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """json string method"""
        if isinstance(list_dictionaries, list):
            if list_dictionaries is None or list_dictionaries == []:
                return "[]"
            else:
                json_string = json.dumps(list_dictionaries)
        return json_string
    
    @staticmethod
    def from_json_string(json_string):
        """Returns Python obj of JSON string representation"""
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        list_dicts = []
        if list_objs is not None:
            for obj in list_objs:
                list_dicts.append(cls.to_dictionary(obj))
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        """Returns instance with attributes already set"""
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instance
        """
        filename = cls.__name__ + '.json'
        if path.exists(filename) is False:
            return []
        with open(filename, 'r') as fd:
            attrs_dic = cls.from_json_string(fd.read())
            li = []
            for i in attrs_dic:
                li.append(cls.create(**i))
            return li
