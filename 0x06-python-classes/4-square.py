#!/usr/bin/python3
'''Module contains square class declaration'''


class Square:
    '''A square class'''
    def __init__(self, size=0):
        '''instatiating a class'''
        self.__square_size = size

    @property
    def size(self):
        '''size getter function'''
        return self.__square_size

    @size.setter
    def size(self, size):
        '''size setter function'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__square_size = size

    def area(self):
        '''Returns the area of a square'''
        s = self.__square_size
        return (s * s)
