#!/usr/bin/python3
"""
    Testing max_integer([]) with unittest
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
