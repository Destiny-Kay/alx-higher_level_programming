#!/usr/bin/python3
'''Appending text to a file'''


def append_write(fielname="", text=""):
    '''
    Appends text to a file
    Args:
        filename: name of file
        text: text to be appended to the file
    '''
    with open(fielname, "a", encoding="utf-8") as f:
        return f.write(text)
