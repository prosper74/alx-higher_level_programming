#!/usr/bin/python3
"""Square object that can print squares"""


class Square:
    'Square object that can print squares'

    def __init__(self, size=0, position=(0, 0)):
        'Initialize data'
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if len(position) != 2 or isinstance(position, tuple) is not True:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(position[0], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(position[1], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        'Method to set self.__size'
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        'Returns the square of size'
        if isinstance(self.__size, int) is not True:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
        return self.__size**2

    @property
    def position(self):
        'Method to position square'
        return self.__position

    @position.setter
    def position(self, value):
        'Sets positon'
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(value, tuple) is not True:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(value[0], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(value[1], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        'Method to print square'
#        if self.__position[0] > 0:
#        	print('' * self.__position[1])
        if self.__size == 0:
            print("")
        else:
            print('\n' * self.__position[1], end='')
        for i in range(self.__size):
            print(" " * self.__position[0], end='')
            print("#" * self.__size)
