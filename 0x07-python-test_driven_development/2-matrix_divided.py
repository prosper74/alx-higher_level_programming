#!/usr/bin/python3
"""
This is the ``Matrix`` module

Contains the function ``matrix_divided``
which divides a matrix of ints/floats by a given int
"""


def matrix_divided(matrix, div):
    """
    :param matrix: the matrix to divide.
    :param div: the number of the division.
    Return a new_matrix of all items in matrix divided by div, all items in
    new_matrix should be floats rounde to 2 decimal points max
    """
    lengths = []
    new_matrix = []
    type_error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or not matrix:
        raise TypeError(type_error)
    for i in matrix:
        quotients = []
        if not isinstance(i, list) or not i:
            raise TypeError(type_error)
        for x in i:
            if not isinstance(x, int) and not isinstance(x, float):
                raise TypeError(type_error)
            quotients.append(round(x / div, 2))
        length = len(i)
        if length not in lengths:
            lengths.append(length)
        new_matrix.append(quotients)
    if len(lengths) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    return new_matrix
