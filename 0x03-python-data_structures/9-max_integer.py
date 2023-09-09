#!/usr/bin/python3

def max_integer(my_list=[]):
    """finds the biggest integer of a list"""
    if len(my_list) <= 0:
        return None
    big_int = 0
    for num in my_list:
        if num > big_int:
            big_int = num
    return big_int
