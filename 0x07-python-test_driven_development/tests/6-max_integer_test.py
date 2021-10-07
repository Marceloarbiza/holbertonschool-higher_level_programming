#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
        Test cases for max_integer
    """
    def test_basic_case(self):
        """ Test the base case
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_basic_case(self):
        """ Test the base case
        """
        self.assertEqual(max_integer([1, 2, 8, 4]), 8)

    def test_same_number(self):
        """ Test the same number
        """
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_empty_list(self):
        """ Test empty list
        """
        self.assertEqual(max_integer([]), None)

    def test_none_list(self):
        """ Test None list
        """
        self.assertEqual(max_integer([None]), None)

    def test_pos_neg(self):
        """ Test positive and negative numbers
        """
        self.assertEqual(max_integer([2, -3, 1, -4]), 2)

    def test_char_letters(self):
        """ Test char letters
        """
        self.assertEqual(max_integer(['b', 'a', 'f', 'c']), 'f')

    def test_char_int(self):
        """ Test char int
        """
        self.assertRaises(TypeError, max_integer, [2, 'f', 5, 'r'])

    def test_char_string(self):
        """ Test string in list
        """
        self.assertRaises(TypeError, max_integer, [2, "dog", 5, "cat"])
