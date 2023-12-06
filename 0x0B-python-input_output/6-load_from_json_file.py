#!/usr/bin/python3
'''creates an object from a JSON file'''
import json


def load_from_json_file(filename):
    '''
    Loads JSON data from a json file
    Args:
        filename: name of the json file
    '''
    with open(filename) as f:
        json.load(f)
