#!/usr/bin/python3
"""
==========================================
appends a string at the end of a text file
==========================================
"""


def append_write(filename="", text=""):
    """ open/create the file and with 'a'
        add to the end of the file
    """

    with open(filename, 'a') as f:
        m = f.write(text)
    return m
