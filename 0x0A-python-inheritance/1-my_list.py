#!/usr/bin/python3
"""MyList"""


class MyList(list):
    """class my list"""
    def print_sorted(self):
        """print_sorted"""
        print(sorted(self))
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
