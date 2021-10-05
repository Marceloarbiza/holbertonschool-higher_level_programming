#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ Test the base case
    """
    def basic_case(self):
        self.assertEqual(max_integer([1, 2, 8, 4]), 8)

    """ Test the same number
    """
    def same_number(self):
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    """ Test the same number
    """
    def empty_list(self):
        self.assertEqual(max_integer([]), None)

    """ Test positive and negative numbers
    """
    def pos_neg(self):
        self.assertEqual(max_integer([2, -3, 1, -4]), 2)

    """ Test char letters
    """
    def char_letters(self):
        self.assertEqual(max_integer(['b', 'a', 'f', 'c']), 'f')

if __name__ == '__main__':
    unittest.main()
