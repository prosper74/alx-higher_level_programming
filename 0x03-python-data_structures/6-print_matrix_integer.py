#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    for _ in matrix:
        for j in matrix[i]:
            print("{:d}".format(j), end="")

            if j != matrix[i][-1]:
                print(" ", end="")

        print("")
        i += 1
