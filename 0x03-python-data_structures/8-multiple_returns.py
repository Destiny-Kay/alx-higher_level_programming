#!/usr/bin/python3

def multiple_returns(sentence):
    """returns a tuple with the length of a string
        as its first character"""
    if sentence == "":
        ret_tuple = (len(sentence), None)
        return ret_tuple
    ret_tuple = (len(sentence), sentence[0])
    return ret_tuple
