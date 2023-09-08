#!/usr/bin/python3

def no_c(my_string):
    """removes all characters 'c' & 'C' in a string"""
    for i in range(len(my_string) - 1):
        if my_string[i] == 'C' or my_string == 'c':
            my_string = my_string[:i] + my_string[i + 1:]
    return my_string
