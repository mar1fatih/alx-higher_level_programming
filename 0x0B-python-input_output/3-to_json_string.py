#!/usr/bin/python3
"""3. To JSON string"""


def to_json_string(my_obj):
    """to_json_string"""
    import json
    json_file = json.dumps(my_obj)
    return json_file
