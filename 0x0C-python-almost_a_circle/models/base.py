#!/usr/bin/python3
"""
This module is part of the Python Almost a Circle project.
It includes a Base class
"""

import json
import csv
import turtle


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        JSON serialization: return the JSON string
        representation of list_dictionaries.
        :param list_dictionaries: list of dictionaries to serialize
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Class method that writes the JSON string representation
        of list_objs to a file
        :param list_objs: list of objects to be saved
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Static method that returns the list of the
        JSON string representation json_string
        :param json_string: JSON string representation of the list
        Returns:
            If json_string is None or empty, return an empty list
            Otherwise, return the list represented by json_string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Class method that returns an instance
        with all attributes already set
        :param dictionary: double pointer to dictionary

        Note: **dictionary must be used as **kwargs of the method update
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """
        Class method that returns a list of instances
        Returns:
            If the file doesn’t exist, return an empty list
            Otherwise, return a list of instances
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r", encoding="utf-8") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Class method that serializes and deserializes in CSV
        :param list_objs: list of objects
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="", encoding="utf-8") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Class method that serializes and deserializes in CSV
        :param list_objs: list of objects
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="", encoding="utf-8") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Static method that opens a window and draws
        all the Rectangles and Squares.
        Library: Uses the Turtle graphics module
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#311042")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for _ in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#9932CC")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for _ in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
