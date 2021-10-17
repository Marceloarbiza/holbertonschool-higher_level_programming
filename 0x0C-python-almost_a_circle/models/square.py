#!/usr/bin/python3
"""
=========================================================
Creation of the class Square that inherits from Rectangle
=========================================================
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor of Square """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """  return [Square] (<id>) <x>/<y> - <size> """
        strRet = ""
        if self.width == 0 or self.height == 0:
            return strRet
        else:
            return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                    self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ getter size """

        return self.width

    @size.setter
    def size(self, value):
        """ setter size """

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ assigns attributes """

        if len(args) > 0:
            for a in range(len(args)):
                if a == 0:
                    self.id = args[0]
                if a == 1:
                    self.size = args[1]
                if a == 2:
                    self.x = args[2]
                if a == 3:
                    self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
