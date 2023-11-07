#!/usr/bin/python3
"""5. Save Object to a file"""


def save_to_json_file(my_obj, filename):
    """save_to_json_file"""
    import json
    with open(filename, "w", encoding="UTF8") as file:
        json_file = json.dumps(my_obj)
        file.write(json_file)
