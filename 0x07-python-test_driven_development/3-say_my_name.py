#!/usr/bin/python3
"""
    Print the first and last name
"""


def say_my_name(first_name, last_name=""):
    """
    This function must print the first and last name.

    Both must be strings.
    """
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
