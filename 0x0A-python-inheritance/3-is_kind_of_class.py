#!/usr/bin/python3
'''function to determine whether an object os an instance'''


def is_kind_of_class(obj, a_class):
    '''
    checks whether an obj is an instance of a_class
    Returns:
        True if obj isinstance of a_class
        False otherwise
    '''
    return isinstance(obj, a_class)
