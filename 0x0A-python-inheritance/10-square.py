#!/usr/bin/python3
""" Write a class BaseGeometry (based on 6-base_geometry.py).
"""


""" Import class BaseGeometry """
BaseGeometry = __import__('9-rectangle').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class Rectangle heridate from BaseGeometry """
    def __init__(self, width, height):

        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)

    """ the area for Rectangle """
    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))


class Square(Rectangle):
    """ Class Square heridate from Rectangle """
    def __init__(self, size):

        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return ("[Rectangle] {:d}/{:d}".format(self.__size, self.__size))
