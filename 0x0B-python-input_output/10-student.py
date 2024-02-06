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
        """
        Initialize the Student
        :param first_name: Name of the person.
        :param last_name: Name of the person
        :param age: Number of years of the person
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Function that retieve a dictoionary representation
        :param attrs: attributes to be converted
        """
        if attrs is None:
            return self.__dict__
        return {key: value for key,
                value in self.__dict__.items() if key in attrs}
