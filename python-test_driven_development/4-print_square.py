#!/usr/bin/python3
"""print_square function"""


def print_square(size):
    """function that prints a square"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
