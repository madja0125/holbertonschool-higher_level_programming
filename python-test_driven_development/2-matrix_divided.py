#!/usr/bin/python3

"""
matrix_divided function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    matrix_divided divide all elements by div
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for list in matrix:
        if len(list) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []

        for element in list:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
            else:
                new_row.append(round(element / div, 2))

        new_matrix.append(new_row)

    return new_matrix
