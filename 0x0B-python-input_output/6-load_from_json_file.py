#!/bin/usr/python3
"""6. Create object from a JSON file"""


def load_from_json_file(filename):
    """load_from_json_file"""
    import json
    with open(filename, "r", encoding="UTF8") as file:
        json_object = json.load(file)
    return json_object
