#!/usr/bin/python3
'''A rectangle definition'''


class Rectangle:
    '''A rectangle class'''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''class initializer'''
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        return (self.__width + self.__height) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''static method that returns the biggest rectangle'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        '''string representation of the rectangle'''
        if self.__width == 0 or self.height == 0:
            return ""
        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        '''string representation of the class'''
        return "Rectangle({}, {})".format(self.__width, self.height)

    def __del__(self):
        '''function that runs when an instance is deleted'''
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @classmethod
    def square(cls, size=0):
        '''returns a new rectangle instance with  same width and height'''
        return cls(width=size, height=size)
