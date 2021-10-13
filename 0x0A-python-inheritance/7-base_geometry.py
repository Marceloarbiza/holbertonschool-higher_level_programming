#!/usr/bin/python3
"""
===============================
Module class 7-base_geometry.py
===============================
"""


class BaseGeometry:
    """ functions of BaseGeometry """

    def area(self):
        """ the area """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer validator """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
