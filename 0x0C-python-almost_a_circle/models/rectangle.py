#!/usr/bin/python3
"""
This module is part of the Python Almost a Circle project.
It includes a class 'Rectangle' that inherits from Base
"""

from models.base import Base


class Rectangle(Base):
    """Represent a rectangle class that inherits fron Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle constructor.
        :param width: width of the rectangle.
        :param height: height of the rectangle.
        :param x: x coordinate of the rectangle.
        :param y: y coordinate of the rectangle.
        :param id: id of the rectangle
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
