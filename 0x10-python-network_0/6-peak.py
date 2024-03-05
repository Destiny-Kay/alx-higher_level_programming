#!/usr/bin/python3
#Peaky finder


def find_peak(list_of_integers):
    '''Finds the peak from a list of integers'''
    if len(list_of_integers) < 1:
        return None
    peak = 0
    start = list_of_integers[0]
    index = 0
    while index < len(list_of_integers):
        if list_of_integers[index] >= start:
            if list_of_integers[index] > peak:
                peak = list_of_integers[index]
            start = list_of_integers[index]
        index+=1
    return peak
