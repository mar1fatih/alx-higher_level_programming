#!/usr/bin/python3
"""base module"""


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init method"""
        if not id:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert list of dict to json str"""
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        import json
        return json.dumps(list_dictionaries)
