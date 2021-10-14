#!/usr/bin/python3
"""
===========================================================
Write a function that inserts a line of text to a file,
after each line containing a specific string (see example):
===========================================================
"""


def append_after(filename="", search_string="", new_string=""):
    """ write an specific line """

    text = ""
    with open(filename, 'r') as re:
        for line in re:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, 'w') as wr:
        wr.write(text)
