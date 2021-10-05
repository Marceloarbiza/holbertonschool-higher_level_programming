#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def basic_case(self):
        """ Test the base case
        """
        self.assertEqual(max_integer([1, 2, 8, 4]), 8)

    def same_number(self):
        """ Test the same number
        """
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def empty_list(self):
        """ Test empty list
        """
        self.assertEqual(max_integer([]), None)

    def none_list(self):
        """ Test None list
        """
        self.assertEqual(max_integer([None]), None)

    def pos_neg(self):
        """ Test positive and negative numbers
        """
        self.assertEqual(max_integer([2, -3, 1, -4]), 2)

    def char_letters(self):
        """ Test char letters
        """
        self.assertEqual(max_integer(['b', 'a', 'f', 'c']), 'f')

    def char_int(self):
        """ Test char int
        """
        self.assertRaises(TypeError, max_integer, [2, 'f', 5, 'r'])

    def char_string(self):
        """ Test string in list
        """
        self.assertRaises(TypeError, max_integer, [2, "dog", 5, "cat"])
