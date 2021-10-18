#!/usr/bin/python3
"""
========================
All tests for Class Base
========================
"""

from models.base import Base
from models.rectangle import Rectangle
import unittest


class TestCaseBase(unittest.TestCase):

    def test_args(self):
        """ test differents types of args """

        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        b6 = Base(-3)
        b7 = Base('a')
        b8 = Base("hello")
        b9 = Base(None)
        b10 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)
        self.assertEqual(b6.id, -3)
        self.assertEqual(b7.id, 'a')
        self.assertEqual(b8.id, "hello")
        self.assertEqual(b9.id, 5)
        self.assertEqual(b10.id, 6)

    def test_to_json_string(self):
        """ try func to_json_string """

        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        
        self.assertTrue(type(dictionary), dict)
        self.assertTrue(type(json_dictionary), str)
        
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")
