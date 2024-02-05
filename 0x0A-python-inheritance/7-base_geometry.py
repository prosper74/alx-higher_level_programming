#!/usr/bin/python3
"""
This module is part of the Python Inheritance project
Defines an empty class BaseGeometry.
"""


class BaseGeometry:
    """
    Represent base geometry class.
    """

    def area(self):
        """
        Not implemented.
        Raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate a parameter as an integer.
        :param self: the default contructor
        :param name: The name of the parameter.
        :param value: The value of the parameter
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
