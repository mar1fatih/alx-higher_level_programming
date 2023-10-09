#!/usr/bin/python3
"""sorted list"""


class MyList(list):
    """MyList"""
    def print_sorted(self):
        """print_sorted"""
        sorted_list = sorted(self)
        print(sorted_list)
