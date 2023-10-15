#!/usr/bin/python3
'''MyInt class definition'''


class MyInt(int):
    '''MyInt class definition'''
    def __eq__(self, other):
        '''modifies the behaviour of the equality operator'''
        return not super().__eq__(other)

    def __ne__(self, other):
        '''modifies the behaviour of != operator'''
        return not super().__ne__(other)
