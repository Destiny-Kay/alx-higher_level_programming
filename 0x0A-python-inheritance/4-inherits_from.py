#!/usr/bin/python3
'''obj checking'''


def inherits_from(obj, a_class):
    '''
    Returns True if an object inherits from a_class
    '''
    return issubclass(type(obj), a_class) and type(obj) != a_class
