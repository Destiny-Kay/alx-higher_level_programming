#!/usr/bin/python3
'''A class module'''


class Square:
    ''' a square class'''
    def __init__(self, size=0, position=(0, 0)):
        self.__square_size = size
        self.__square_position = position

    @property
    def size(self):
        '''size getter'''
        return self.__square_size

    @size.setter
    def size(self, value):
        '''size setter'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        self.__square_size = value

    @property
    def position(self):
        '''position getter'''
        return self.__square_position

    @position.setter
    def position(self, value):
        '''position setter'''
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__square_position = value

    def area(self):
        '''returns the area of a square'''
        s = self.__square_size
        return s * s

    def my_print(self):
        '''prints a square with #'''
        s = self.__square_size
        if s == 0:
            print("")
            return
        for i in range(0, self.__square_size):
            [print(" ", end="") for j in range(0, self.__square_position[0])]
            [print("#", end="") for k in range(0, self.__square_size)]
            print("")
