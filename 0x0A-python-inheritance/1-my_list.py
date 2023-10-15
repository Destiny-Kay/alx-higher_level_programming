#!/usr/bin/python3
"""Mylist class definition"""


class MyList(list):
    '''Mylist class definition'''
    def print_sorted(self):
        '''prints Mylist in a sorted(ascending) order'''
        print(sorted(self))
