#!/usr/bin/python3
"""
    ============================================
    Write a class Student that defines a student
    ============================================
"""


class Student:
    """ init the class attributes """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ return this class in a dict representation for json """

        if attrs is None:
            return self.__dict__
        else:
            dictRet = {}
            for a in attrs:
                if hasattr(self, a):
                    dictRet[a] = getattr(self, a)
            return dictRet
