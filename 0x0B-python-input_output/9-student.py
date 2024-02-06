#!/usr/bin/python3
"""
This module is part of the Python Input Output project.
A class Student that defines a student by
public instance attributes.
"""


class Student:
    """
    class Student that defines a student by public
    instance attributes - first_name, last_name, age
    """
    def __init__(self, first_name, last_name, age):
        """Initialize the Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student"""
        return self.__dict__
