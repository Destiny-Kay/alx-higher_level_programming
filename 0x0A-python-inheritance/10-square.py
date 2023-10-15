#!/usr/bin/python3
'''A square class definition'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''The rectangle class definition'''
    def __init__(self, size):
        '''Square class instantiation'''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
