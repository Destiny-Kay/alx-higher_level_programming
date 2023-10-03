#!/usr/bin/python3
'''Rectangle'''


class Rectangle:
    '''
    A rectangle class

    Args:
        width- postive integer
        height- positive integer
    Attr:
        perimeter-finds the perimeter of the rectangle
    '''
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        '''class initializer'''
        self.__height = height
        self.__width = width
        type(self).number_of_instances += 1

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
        '''height getter function'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height setter'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''returns the area of the rectangle'''
        return self.__height * self.__width

    def perimeter(self):
        '''returns the perimeter of the rectangle'''
        if self.__height == 0 or self.width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        '''string representation of the rectangle'''
        if self.__width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for i in range(self.height):
            for j in range(self.__width):
                rectangle_str += "#"
            rectangle_str += "\n"
        return rectangle_str

    def __repr__(self):
        '''A rectangle repr string'''
        return "Rectangle({}, {})".format(self.__width, self.height)

    def __del__(self):
        '''prints a message when a rectangle object is deleted'''
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
