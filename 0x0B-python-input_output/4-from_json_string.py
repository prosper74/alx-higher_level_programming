#!/usr/bin/python3
"""
This module is part of the Python Input Output project.
Defines a function that returns object (Python data structure).
"""

import json


def from_json_string(my_str):
    """
    A function that returns an object (Python data structure)
    represented by a JSON string
    :param my_str:  The JSON string
    Returns the JSON representation
    """
    return json.loads(my_str)
