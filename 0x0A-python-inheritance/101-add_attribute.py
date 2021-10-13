#!/usr/bin/python3
"""
==========================
Module class new attribute
==========================
"""


def add_attribute(obj, name, value):
    """ add a new attribute """

    if hasattr(obj, '__dict__') is True:
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
