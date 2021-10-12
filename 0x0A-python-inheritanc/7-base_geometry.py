#!/usr/bin/python3
""" Write a class BaseGeometry (based on 6-base_geometry.py).
"""


class BaseGeometry:

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.value = value
        self.name = name

        if isinstance(self.value, int) is False:
            raise TypeError("{} must be an integer".format(self.name))
        if self.value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
