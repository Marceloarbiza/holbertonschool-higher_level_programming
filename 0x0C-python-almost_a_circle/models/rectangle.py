#!/usr/bin/python3
"""
=======================================================
Creation if the class Rectabgle that inherits from Base
=======================================================
"""

from models.base import Base


class Rectangle(Base):
    """ class Rectangle from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init Rectangle class """

        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter width """

        return self.__width

    @width.setter
    def width(self, value):
        """ setter width """

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ getter height """

        return self.__height

    @height.setter
    def height(self, value):
        """ setter height """

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ getter x """

        return self.__x

    @x.setter
    def x(self, value):
        """ setter x """

        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ getter y """

        return self.__y

    @y.setter
    def y(self, value):
        """ setter y """

        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ area of the rectangle """

        return self.__width * self.__height

    def display(self):
        """ display prints in stdout the Rectangle """

        if self.width == 0 or self.height == 0:
            print("")
            return

        for i in range(self.__y):
            print()
        for h in range(self.__height):
            for s in range(self.__x):
                print(" ", end="")
            for w in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """ returns [Rectangle] (<id>) <x>/<y> - <width>/<height> """

        strRet = ""
        if self.__width == 0 or self.__height == 0:
            return strRet
        else:
            return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ that assigns an argument to each attribute """

        if len(args) > 0:
            for a in range(len(args)):
                if a == 0:
                    self.id = args[a]
                if a == 1:
                    self.__width = args[a]
                if a == 2:
                    self.__height = args[a]
                if a == 3:
                    self.__x = args[a]
                if a == 4:
                    self.__y = args[a]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle """

        return {
            'id': self.id, 'width': self.width,
            'height': self.height, 'x': self.x, 'y': self.y
        }
