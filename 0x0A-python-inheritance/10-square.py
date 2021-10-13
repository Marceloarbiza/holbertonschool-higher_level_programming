#!/usr/bin/python3
""" Write a class BaseGeometry (based on 6-base_geometry.py).
"""


""" Import class Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square heridate from Rectangle """
    def __init__(self, size):

        self.__size = size
        self.integer_validator("size", size)

    """ the area for Square """
    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return ("[Rectangle] {:d}/{:d}".format(self.__size, self.__size))
