#!/usr/bin/python3
"""
This module contains one function: add_integer(a, b)
The module is part of the Python test driven development
add_integer(a, b): Return the result of a + b
"""


def add_integer(a, b):
    """
    :param a: the first number.
    :param b: the second number.
    Return int(a) + int(b)
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
