#!/usr/bin/python3
"""7. Load, add, save"""


from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
i = 1
list_t = []
if len(argv) > 1:
    for i in range(1, len(argv)):
        list_t = load_from_json_file("add_item.json")
        list_t.append(argv[i])
        save_to_json_file(list_t, "add_item.json")
else:
    save_to_json_file(list_t, "add_item.json")
