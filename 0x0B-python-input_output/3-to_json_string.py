#!/usr/bin/python3
'''jsonifies an object'''
import json


def to_json_string(my_obj):
    '''
    Returns the json representation of an object
    Args:
        my_obj: object to be jsonified
    '''
    return json.dumps(my_obj)
