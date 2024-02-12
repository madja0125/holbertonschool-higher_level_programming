#!/usr/bin/python3

"""module that converts a json string to a python object"""

import json


def from_json_string(my_str):
    """function that converts the json string to an object"""
    obj = json.loads(my_str)
    return obj
