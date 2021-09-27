#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        n = int(value)
        print("{:d}".format(n))
        return True
    except ValueError:
        sys.stderr.write("Exception: Unknown format code 'd' \
                for object of type 'str'\n")
        return False
