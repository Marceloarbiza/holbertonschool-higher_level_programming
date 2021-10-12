#!/usr/bin/python3
""" Write a class BaseGeometry (based on 6-base_geometry.py).
"""


class BaseGeometry:
    """ functions """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        if isinstance(value, int) is False:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Class Rectangle heridate from BaseGeometry """
    def __init__(self, width, height):

        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)

    """ the area for Rectangle """
    def area(self):
        print("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
        return self.__width * self.__height
