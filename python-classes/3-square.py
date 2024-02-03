#!/usr/bin/python3

"""
module: 3-square
class Square
"""


class Square:
    """
    Square class
    """

    def __init__(self, size=0):
        """
        defining size to ssquare if size is
        an int and bigger than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        return the area of square
        """
        return self.__size ** 2
