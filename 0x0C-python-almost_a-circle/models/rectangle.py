#!/usr/bin/python3
'''Class rectangle that inherits from the base class'''
from .base import Base


class Rectangle(Base):
    '''A rectangle class'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''Class instatiator'''
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        '''width getter function'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Width setter function'''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        '''height attr getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height attr setter'''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        '''x attr property getter'''
        return self.__x

    @x.setter
    def x(self, value):
        '''x attribute setter'''
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        '''y attr getter'''
        return self.__y

    @y.setter
    def y(self, value):
        '''y attr setter'''
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''returns the area of a rectangle'''
        return self.__width * self.__height
###question 5
    def display(self):
        '''Displays a rectangle object printed out using a symbol'''
        print_ele = ''
        for i in range(self.__height):
            print_ele+=[print_ele+='#' for j in range()]

