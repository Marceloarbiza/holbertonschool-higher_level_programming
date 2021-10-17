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
