#!/usr/bin/python3

"""class Mylist"""


class MyList(list):
    """class that sort a list"""

    def print_sorted(self):
        """method that sort a list"""
        if isinstance(self, list):
            sortlist = sorted(self)
            print(sortlist)
