#!/usr/bin/python3

"""
This module is part of the Python Inheritance project.
Defines a function that adds attributes to objects.
"""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible.
    :param obj: the object to add
    :param att: the attribute
    :param value: the attribute value
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
