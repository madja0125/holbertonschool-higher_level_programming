#!/usr/bin/python3

"""Module that have a class that inherits from other one"""


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


class Rectangle(BaseGeometry):
    """class inherited from Basegeometry"""

    def __init__(self, width, height):
        """Method that set width and height private and
        validate that they are positive integers"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
