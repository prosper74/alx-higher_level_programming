#!/usr/bin/python3
"""
This module is part of the Python Input Output project.
Inserts a line of text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """
    A function that inserts a line of text to a file,
    after each line containing a specific string
    """
    with open(filename, "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + "\n")
        file.truncate()
