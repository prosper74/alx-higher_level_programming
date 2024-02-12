#!/usr/bin/python3
"""
This module is part of the Python Almost a Circle project.
It includes a class 'Square' that inherits from Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square constructor.
        :param size: size of the square (integer).
        :param x: x coordinate of the square.
        :param y: y coordinate of the square.
        :param id: id of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size of the square
        :param value: value to set
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the Square class.
        :param args: arguments to pass to the method
        :param kwargs: additional keyword arguments to pass to the method
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """
        Public method that return the dictionary
        representation of the Square.
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
