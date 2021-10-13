#!/usr/bin/python3
"""
=============================
Write a string to a text file
and return the num of chars
=============================
"""


def write_file(filename="", text=""):
    """ open file with w condition i can write in it
        if the file doesnt exist, create it automatically
    """

    with open(filename, 'w') as f:
        """ f.write add the content to the file
        and return the number of chars writed
        """

        m = f.write(text)
    return m
