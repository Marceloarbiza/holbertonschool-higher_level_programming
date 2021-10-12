#!/usr/bin/python3
""" Write a class MyInt that inherits from int
"""


class MyInt(int):
    """ Rebel """
    def __eq__(self, other):
        return not super().__eq__(other)

    def __ne__(self, other):
        return not super().__ne__(other)
