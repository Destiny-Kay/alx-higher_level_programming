#!/usr/bin/python3
'''Defines a function that returns the JSON representation of an object'''
import json


def from_json_string(my_str):
    """Return the Python object representation of a JSON string."""
    return json.loads(my_str)
