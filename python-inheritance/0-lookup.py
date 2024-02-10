#!/usr/bin/python3
"""function that returns a list of available
attributes and methods of an object"""


def lookup(obj):
    """lookup function"""
    a = list(dir(obj))
    return a
