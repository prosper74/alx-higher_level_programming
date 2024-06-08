#!/usr/bin/python3
""" Square object class """


class Square:
    'Square object class'

    def __init__(self, size=0):
        'Initialize data'
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        'Method to set self.__size'
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        self.__size = value

    def area(self):
        'Method to square self.__size'
        if isinstance(self.__size, int) is not True:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
        return self.__size**2
