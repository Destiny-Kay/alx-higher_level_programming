#!/usr/bin/python3
'''Defines a function that prints a square with the # character'''


def print_square(size):
    '''
    prints a square using the # symbol\n
    Args:
        size: the size of the square to be printed
    '''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        [print("#", end="") for j in range (size)]
        print("")