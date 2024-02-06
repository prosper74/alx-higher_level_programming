#!/usr/bin/python3
"""
This module is part of the Python Inheritance project
Defines a class Rectangle that inherits from BaseGeometry.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """
        Initialize a new square.
        :param size: The size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size