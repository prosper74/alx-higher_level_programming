#!/usr/bin/python3

"""
This is the ``Square`` module
The module is part of the Python test driven development
It contains a the ``print_square`` function
The function prints a square of '#'s
"""


def print_square(size):
    """
    print out a square of given size
    :param size: size of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for col in range(size):
        for row in range(size):
            print("#", end="")
        print("")
