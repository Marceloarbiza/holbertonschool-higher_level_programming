#!/usr/bin/python3
"""
    Prints a square with the character #
"""


def print_square(size):
    """
    This function must print a square with #.

    The size is the length a weight.

    The size must be a positive number or 0
    """
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print('#', end="")
        print()
