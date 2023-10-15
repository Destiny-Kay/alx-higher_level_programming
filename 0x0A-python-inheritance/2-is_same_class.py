#!/usr/bin/python3
'''checks whether an object os an instance of a class'''


def is_same_class(obj, a_class):
    '''
    checks whether obj is an instance of a_class
    Returns:
        True: if obj isinstance of a_class
        else false
    '''
    if type(obj) == a_class:
        return True
    return False
