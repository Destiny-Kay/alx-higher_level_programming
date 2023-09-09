#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """deletes an element at idx from the list"""
    if idx >= len(my_list) - 1 or idx < 0:
        return my_list
    new_list = []
    for i in range(len(my_list) - 1):
        if i != idx:
            new_list.append(my_list[i])
    return new_list
