#!/usr/bin/python3
"""
=============================================
Module class def inherits_from(obj, a_class):
=============================================
"""


def inherits_from(obj, a_class):
    """ look if the object is an instance of a class """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
