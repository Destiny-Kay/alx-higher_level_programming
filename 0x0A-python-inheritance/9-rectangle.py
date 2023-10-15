#!/usr/bin/python3
'''Rectangle class definition'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle class definition'''
    def __init__(self, width, height):
        '''Instantiates the rectangle class'''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        '''returns the area of the rectangle instance'''
        return self.__height * self.__width

    def __str__(self):
        '''the string representation for class'''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
