#!/usr/bin/python3
'''Add two integers'''


def add_integer(a, b=98):
    '''
    Adds two integers
    Args:
        a: integer or float value
        b: integer or float value
    Return: the sum of a and b
    '''
    if not a:
        return
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
