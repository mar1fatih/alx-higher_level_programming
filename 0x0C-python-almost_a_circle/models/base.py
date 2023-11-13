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

    @classmethod
    def save_to_file(cls, list_objs):
        """save the object attribute to a file"""
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            _list = []
            for ls in list_objs:
                _list.append(ls.to_dictionary())
            f.write(cls.to_json_string(_list))

    @staticmethod
    def from_json_string(json_string):
        """extract the list from json str"""
        import json
        return json.loads(json_string)
