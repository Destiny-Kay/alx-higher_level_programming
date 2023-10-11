#!/usr/bin/python3
'''Defines a function that reads a file'''


def read_file(filename=""):
    """
    reads a file and prints the contents to the standard output
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
