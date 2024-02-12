#!/usr/bin/python3
"""
module contains a class names Square
that inherited from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square is a child class from Rectangle
    """

    def __init__(self, size):
        """ initialize square class by assigning the size"""
        self.__size = size
        super().integer_validator("size", size)

    def area(self):
        """ returns the area of the square """
        return self.__size ** 2

    def __str__(self):
        """
        prints square description
        """
        return f"[Square] {self.__size}/{self.__size}"
