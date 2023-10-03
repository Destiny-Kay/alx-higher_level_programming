#!/usr/bin/python3
'''Rectangle'''


class Rectangle:
    '''
    A rectangle class

    Args:
        width- positive integer
        height- positive integer
    '''
    def __init__(self, width=0, height=0):
        '''class initiator'''
        self.__height = height
        self.__width = width
    
    @property
    def width(self):
        '''width getter'''
        return self.__width
    
    @width.setter
    def width(self, value):
        '''width setter'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        '''height getter'''
        return self.__height
    
    @height.setter
    def height(self, value):
        '''height setter'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value