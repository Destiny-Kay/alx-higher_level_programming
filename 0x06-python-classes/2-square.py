#!/usr/bin/python3
'''Module contains square class declaration'''


class Square:
    '''A square class'''
    def __init__(self, size=0):
        '''Initializing the class with an optional size'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
