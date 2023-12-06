#!/usr/bin/python3
'''Inserts a line of text to a file that meets a certain criterion'''


def append_after(filename="", search_string="", new_string=""):
    '''
    Appends a string to a file after a search pattern in met
    Args:
        filename: name of the file
        search-string: search pattern to be looked for
        new_string: the nw string to be appended
    '''
    text = ''
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, 'w') as w:
        w.write(text)
