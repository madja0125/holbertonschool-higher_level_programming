#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    if matrix is None:
        return

    for row in matrix:
        for i, digit in enumerate(row):
            if i != 0:
                print(" ", end="")
            print("{:d}".format(digit), end='')
        print()
