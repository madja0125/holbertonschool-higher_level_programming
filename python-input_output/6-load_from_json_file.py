#!/usr/bin/python3

"""Module that creates an Object from JSON file"""

import json


def load_from_json_file(filename):
    """function that creates an object from a json file"""
    with open(filename, "r") as file:
        return json.load(file)
