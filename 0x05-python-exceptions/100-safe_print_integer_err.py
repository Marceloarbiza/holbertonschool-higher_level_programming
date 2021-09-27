#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        n = int(value)
        print("{:d}".format(n))
        return True
    except ValueError as er:
        print("Exception:", er)
        return False
