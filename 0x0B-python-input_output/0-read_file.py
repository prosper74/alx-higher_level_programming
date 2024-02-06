#!/usr/bin/python3

"""
This module is part of the Python Input Output project.
Defines a function that reads a text file.
"""


def read_file(filename=""):
    """
    A function that reads a text file (UTF8) and prints it to stdout
    :param filename: The filename of the text file
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
