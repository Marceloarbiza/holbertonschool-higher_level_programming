#!/usr/bin/python3
"""
===========================================================
Write a function that inserts a line of text to a file,
after each line containing a specific string (see example):
===========================================================
"""


def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r') as re:
        for line in re:
            if search_string in re:
                re.write(new_string)
