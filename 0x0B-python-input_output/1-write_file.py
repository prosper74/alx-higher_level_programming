#!/usr/bin/python3

"""
This module is part of the Python Input Output project.
Defines a function that writes a text to a file.
"""


def write_file(filename="", text=""):
    """
    A function that writes a string to a text file (UTF8)
    and returns the number of characters written
    :param filename: The filename of the text file
    :param text: The string to write to the file

    Returns the number of characters written to the file
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
