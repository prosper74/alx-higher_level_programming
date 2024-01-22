#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    result_matrix = []

    for row in matrix:
        squared_row = [num ** 2 for num in row]
        result_matrix.append(squared_row)

    return result_matrix
