#!/usr/bin/python3

"""Module with one class and two public methods"""


class BaseGeometry:
    """Class that have the method"""

    def area(self):
        """method that raise en message error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that validates value"""
        if isinstance(name, str):
            if type(value) is not int:
                raise TypeError(f"{name} must be an integer")
            if value <= 0:
                raise ValueError(f"{name} must be greater than 0")
