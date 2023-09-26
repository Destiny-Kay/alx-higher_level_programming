#!/usr/bin/python3
class Square:
    '''A square class'''
    def __init__(self, size=0):
        '''Instantiating a class object'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__square_size = size
    
    def area(self):
        '''A public instance method that returns the area of a square'''
        s = self.__square_size
        return (s * s)
