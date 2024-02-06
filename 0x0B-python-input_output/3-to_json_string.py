#!/usr/bin/python3
"""
This module is part of the Python Input Output project.
Defines a function that returns JSON.
"""

import json


def to_json_string(my_obj):
    """
    A function that returns the JSON representation
    of an object (string)
    :param my_obj: the JSON object
    Returns the JSON representation
    """
    return json.dumps(my_obj)
