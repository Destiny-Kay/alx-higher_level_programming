#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """finds the multiples of 2 in a list"""
    divisible = []
    for num in range(len(my_list)):
        if my_list[num] % 2 == 0:
            divisible.append(True)
        else:
            divisible.append(False)
    return divisible
