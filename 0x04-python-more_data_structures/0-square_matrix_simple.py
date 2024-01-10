#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    result_matrix = []

    for row in matrix:
        squared_row = [lambda num: num ** 2, row]
        result_matrix.append(squared_row)

    return result_matrix
