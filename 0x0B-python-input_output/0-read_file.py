#!/usr/bin/python3
'''Reading a utf8 encoded file'''


def read_file(filename=""):
    '''
    Reads a  text file and prints its content to STDOUT
    Args:
        filename: name of the file to be printed out
    '''
    with open(filename, "r", encoding="utf-8") as f:
        file_content = f.read()
        print(file_content, end="")
