#!/bin/usr/python3

def square_matrix_simple(matrix=[]):

    if matrix is None:
        return

    if len(matrix) == 0:
        return

    new_matrix = []

    for i in matrix:
        list = []

        for dgt in i:
            list.append(dgt ** 2)

        new_matrix.append(list)

    return new_matrix
