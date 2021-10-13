#!/usr/bin/python3
"""
==============================================
Module class def __init__(self, width, height)
==============================================
"""


""" Import Module """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class Rectangle heridate from BaseGeometry """

    def __init__(self, width, height):

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
