#!/usr/bin/python3

def print_reversed_list_integer(mylist=[]):
    """prints all integers of a list in reverse"""
    list_range = len(mylist) - 1
    if list_range < 0:
        return
    for i in range(list_range, -1, -1):
        print("{:d}".format(mylist[i]))
