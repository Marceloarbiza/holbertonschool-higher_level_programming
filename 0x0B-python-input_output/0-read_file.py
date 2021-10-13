#!/usr/bin/python3
"""
======================
Reads a text file UTF8
======================
"""


def read_file(filename=""):
    """ open the file """

    with open(filename) as file:
        """ read the file content """

        read_data = file.read()
        """ print the file """

        print(read_data, end="")
