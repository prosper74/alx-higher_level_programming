#!/usr/bin/python3
"""
This module is part of the Python Inheritance project
It has one function - lookup
The function defines an object attribute.
"""


def lookup(obj):
    """
    A function that returns the list of available
    attributes and methods of an object
    """
    return (dir(obj))
