#!/usr/bin/python3
"""
This is the Name module
The module is part of the Python test driven development
This module contains a simple function to print out a first and last name
"""


def say_my_name(first_name, last_name=""):
    """
    :param first_name: the first name.
    :param last_name: the last name.
    Return nothing
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
