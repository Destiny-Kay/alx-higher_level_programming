#!/usr/bin/python3
'''Defines a rectangle class'''
from .base import Base


class Rectangle(Base):
    '''
        The rectangle class\n
        Attr:\n
            width- the width of the rectangle\n
            height- the height of the rectangle\n
            x- x\n
            y- y\n
    '''

    def __init__(self, width,  height, x=0, y=0, id=None):
        '''rectangle class constructor'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''width attr getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''width attr setter'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''height attr getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height attr setter'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''x attr getter'''
        return self.__x

    @x.setter
    def x(self, value):
        '''x attr setter'''
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''y attr getter'''
        return self.__y

    @y.setter
    def y(self, value):
        '''y attr setter'''
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''returns the area of the rectatangle instance'''
        return self.__width * self.__height

    def display(self):
        '''prints the Rectangle to the stdout using #'''
        for i in range(self.__y):
            print("")
        for i in range(self.__height):
            for i in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print('#', end="")
            print("")

    def update(self, *args, **kwargs):
        '''updates the class attributes'''
        if len(args) != 0:
            if len(args) <= 5:
                self.id = args[0] if len(args) >= 1 else self.__id
                self.width = args[1] if len(args) >= 2 else self.__width
                self.height = args[2] if len(args) >= 3 else self.__height
                self.x = args[3] if len(args) >= 4 else self.__x
                self.y = args[4] if len(args) == 5 else self.__y
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        '''Returns the dictionary representation of a rectangle object'''
        dict_repr = {
            'x': self.__x,
            'y': self.__y,
            'id': self.id,
            'height': self.__height,
            'width': self.__width
             }
        return dict_repr

    def __str__(self):
        '''the string representation of the rectangle class'''
        return (
            "[Rectangle] ({}) {}/{} - {}/{}"
            .format(self.id, self.__x, self.__y, self.__width, self.__height)
            )
