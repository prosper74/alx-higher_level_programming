#!/usr/bin/python3
"""
This module is part of the Python Inheritance project
A class MyList that inherits from list
"""


class MyList(list):
    """A class MyList that inherits from list"""

    def print_sorted(self):
        """A that prints the list (sorted in ascending order)"""
        print(sorted(self))
