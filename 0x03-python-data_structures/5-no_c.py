#!/usr/bin/python3
def no_c(my_string):
    new_string = str(my_string)
    leni = len(new_string)
    for i in new_string:
        if i == 'C' and i == 'c':
            i = ' '
    return new_string
