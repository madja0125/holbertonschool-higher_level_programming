#!/usr/bin/python3

"""
module: 5-square
class Square
"""


class Square:
    """
    Square class
    """

    def __init__(self, size=0):
        """
        defining size to square
        """
        self.__size = size

    def area(self):
        """
        return the area of square
        """
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print(chr(35) * self.__size)

    @property
    def size(self):
        """
        returning the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        defining size to square if value is
        an int and bigger than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
