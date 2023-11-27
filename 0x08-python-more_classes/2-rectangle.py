#!/usr/bin/python3
'''A rectangle definition'''


class Rectangle:
    '''A rectangle class'''
    def __init__(self, width=0, height=0):
        '''class initializer'''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''The width getter function'''
        return self.__width

    @width.setter
    def width(self, value):
        '''The width setter function'''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''The height getter function'''
        return self.__height

    @height.setter
    def height(self, value):
        '''The height setter function'''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        '''public instance method that returns the area of the rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''
        public instance method that returns the perimeter of the rectangle
        '''
        if self.__width == 0 or self.height == 0:
            return 0
        return 2 * (self.__width + self.__height)
