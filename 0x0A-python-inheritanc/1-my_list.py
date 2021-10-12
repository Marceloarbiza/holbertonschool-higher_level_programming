#!/usr/bin/python3
""" 
===========================================
Module class MyList that inherits from list
===========================================
"""


class MyList(list):
    """ sorted ordena de forma creciente la lista """

    def print_sorted(self):
        """ print sorted list """

        print(sorted(list(self)))
