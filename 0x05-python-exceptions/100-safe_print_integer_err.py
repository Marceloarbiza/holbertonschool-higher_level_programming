#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        n = int(value)
        print("{:d}".format(n))
        return True
    except ValueError:
        return False
