#!/usr/bin/python3
'''dictionary rep of a DS'''


def class_to_json(obj):
    '''
    Returns a dict description for JSON serialization of an object
    '''
    return obj.__dict__
