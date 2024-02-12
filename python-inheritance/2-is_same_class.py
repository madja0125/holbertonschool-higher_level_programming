#!/usr/bin/python3

"""function that returns True if object is exactly
an instance of the specified class"""


def is_same_class(obj, a_class):
    """function that compares"""
    if type(obj) is a_class:
        if isinstance(obj, a_class):
            return True
    else:
        return False
