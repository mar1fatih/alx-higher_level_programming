#!/usr/bin/python3
"""10. Student to JSON with filter"""


class Student:
    """class Student"""
    def __init__(self, first_name, last_name, age):
        """__init__"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to_json"""
        if attrs is None:
            return self.__dict__
        dict_d = self.__dict__
        dict_t = dict()
        for key, value in dict_d.items():
            for attr in attrs:
                if key == attr:
                    dict_t.update({key: value})
        return dict_t
