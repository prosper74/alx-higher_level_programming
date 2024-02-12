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

    @property
    def width(self):
        """Getter for the width of the Rectangle class"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width of the Rectangle class
        :param value: The value to set the width
        """
        if isinstance(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height of the Rectangle class."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height of the Rectangle class
        :param value: The height of the Rectangle class
        """
        if isinstance(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the x coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x coordinate
        :param value: Value to set the x coordinate
        """
        if isinstance(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for the y coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y coordinate"""
        if isinstance(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Return the area of the Rectangle.
        The area is determined by:
        multiplying the width and height
        """
        return self.width * self.height

    def display(self):
        """
        Print in stdout the Rectangle instance with the character #.
        """
        if self.width == 0 or self.height == 0:
            print("")
            return

        for _ in range(self.y):
            print("")

        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)
