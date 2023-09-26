#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        '''Instatiating a square class'''
        self.__square_size = size
    
    @property
    def size(self):
        '''size getter function'''
        return self.__square_size
    
    @size.setter
    def size(self, size):
        '''size setter function'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__square_size = size
    
    def area(self):
        '''Returns the area of a square'''
        s = self.__square_size
        return (s * s)
    
    def my_print(self):
        '''prints the square with the character #'''
        s = self.__square_size
        if s == 0:
            print("")
        for i in  range(s):
            for j in range(s):
                print("#", end="")
            print("")