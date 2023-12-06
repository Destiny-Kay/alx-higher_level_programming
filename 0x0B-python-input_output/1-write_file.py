#!/usr/bin/python3
'''Writnig a string to a text file'''


def write_file(filename="", text=""):
    '''
    Writes a string to a text file
    Args:
        filename: the name of the file to be modified
        text: text to be written to the file
    Returns:
        number of chars written
    '''
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
