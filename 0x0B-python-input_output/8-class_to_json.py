#!/usr/bin/python3
"""
This module is part of the Python Input Output project.
Defines a function that returns the dictionary description.
"""


def class_to_json(obj):
    """
    A function that returns the dictionary description with
    simple data structure (list, dictionary, string, integer
    and boolean) for JSON serialization of an object
    :param filename: The JSON file
    """
    return obj.__dict__
