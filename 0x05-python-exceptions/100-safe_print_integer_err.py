#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        n = int(value)
        print("{:d}".format(n))
        return True
    except Exception as er:
        print("Exception: {}".format(er), file=sys.stderr)
        return False
