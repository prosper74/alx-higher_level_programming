#!/usr/bin/python3
"""
This module is part of the Python Input Output project.
A class Student that defines a student
"""


class Student:
    """A class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """
        Constructor to initialize a Student
        :param first_name: Name of the student
        :param last_name: Name of the student
        :param age: Number of years of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Converts the student attributes to json
        :param attrs: dict of student attributes"""
        if attrs is None:
            return self.__dict__
        return {key: value for key,
                value in self.__dict__.items() if key in attrs}

    def reload_from_json(self, json):
        """Reload the configuration from the json"""
        for key, value in json.items():
            setattr(self, key, value)
