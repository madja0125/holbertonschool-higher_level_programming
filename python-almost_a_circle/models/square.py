#!/usr/bin/python3
"""Module tha have a class Square that inherits form Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class square"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes istances"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str special method"""
        str_square = "[Square] "
        str_id = f"({self.id}) "
        str_xy = f"{self.x}/{self.y} - "
        str_hw = f"{self.width}"
        str_return = str_square + str_id + str_xy + str_hw
        return str_return

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update method"""
        if args:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """dictionary method """
        dictionary = {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
        return dictionary
