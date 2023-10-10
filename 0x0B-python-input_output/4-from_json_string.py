#!/usr/bin/python3
"""4. From JSON string to Object"""


def from_json_string(my_str):
    """json"""
    import json
    file_json = json.loads(my_str)
    return file_json
