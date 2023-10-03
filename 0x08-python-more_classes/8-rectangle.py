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
    print_symbol = "#"

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.

        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

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
        '''A rectangle repr string'''
        return "Rectangle({}, {})".format(self.__width, self.height)

    def __del__(self):
        '''prints a message when a rectangle object is deleted'''
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
