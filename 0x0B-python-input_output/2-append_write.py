#!/usr/bin/python3

"""
This module is part of the Python Input Output project.
Defines a function that appends a string to a file.
"""


def append_write(filename="", text=""):
    """
    A function that appends a string at the end of a text
    file(UTF8) and returns the number of characters added
    :param filename: The filename to append to.
    :param text: The string to append
    Returns the number of characters
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        return len(text)

