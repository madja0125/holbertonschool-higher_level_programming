#!/usr/bin/python3

"""
Module: 2-quare
Class square
"""


class Square:
    """
    Square class
    """

    def __init__(self, size=0):
        """
        Defining size  to the class Square if
        size is a int and is more than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
