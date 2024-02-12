#!/usr/bin/python3
"""
This module is part of the Python Almost a Circle project.
It includes a Base class
"""


class Base:
    """
    This class will be the “base” of all other classes
    in this project. The goal of it is to manage id attribute
    in all your future classes and to avoid duplicating the same code
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for the class
        :param id: The id of the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
