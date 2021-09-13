#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    leni = len(my_list) - 1
    for leni in range(leni, -1, -1):
        print("{:d}" .format(my_list[leni]))
