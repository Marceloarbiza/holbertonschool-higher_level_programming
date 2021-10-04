#!/usr/bin/python3
"""
    Write a class Rectangle that defines a rectangle
"""


class Rectangle:
    """
        Define __repr__
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        if isinstance(width, int) is False:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")

        if isinstance(height, int) is False:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        cadena = ""
        if self.__width == 0 or self.__height == 0:
            return cadena
        else:
            for h in range(self.__height):
                for w in range(self.__width):
                    cadena += '#'
                cadena += '\n'
        return cadena[0:-1]

    def __repr__(self):
        return 'Rectangle({}, {})'.format(self.__width, self.__height)
