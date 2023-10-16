#!/usr/bin/python3
"""Base clqss"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """__init__ function"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file"""
        new_list = []
        if list_objs is not None:
            for ele in list_objs:
                new_list.append(ele.to_dictionary())
        with open("{}.jason".format(cls.__name__), "w\
                ", encoding="UTF8") as file_j:
            file_j.write(cls.to_jason_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """from_json_string"""
        if json_string and json_string is not None:
            return json.loads(json_string)
        return []
