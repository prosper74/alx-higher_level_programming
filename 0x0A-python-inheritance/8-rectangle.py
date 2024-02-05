#!/usr/bin/python3
"""
This module is part of the Python Inheritance project
Defines a class Rectangle that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry base class."""

    def __init__(self, width, height):
        """
        Intialize a new Rectangle.
        :param width: The width of the rectangle (in int)
        :param height: The height of the rectangle (in int)
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
