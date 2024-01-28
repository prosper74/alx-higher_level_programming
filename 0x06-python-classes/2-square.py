#!/usr/bin/python3

"""
The module is part of the Python test driven development
This module contains one Class: Square.
Define a class Square.
"""


class Square:
    """
    A class Square that defines a square
    """
    def __init__(self, size=0):
        """
        Initialize a new Square constructor.
        Private instance attribute: size.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
