#!/usr/bin/python3
"""
    Add two numbers (integer or float)
"""


def add_integer(a, b=98):
    """
    This function receives 2 numbers as arguments.

    The numbers must be integer or float.

    In the case of receiving only one number, \
        the other number will be 98 by default.

    This function will always return the result \
        as an integer, regardless of receiving integer or float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
