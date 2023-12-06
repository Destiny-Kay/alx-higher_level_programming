#!/usr/bin/python3
'''Writing an object to a text file'''
import json


def save_to_json_file(my_obj, filename):
    '''
    writes an object to a text file using JSON representation
    Args:
        my_obj: object to be written to file
        filename: name of the file to be written to
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
