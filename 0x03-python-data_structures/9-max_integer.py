#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    maxi = 0
    for i in my_list:
        if maxi < i:
            maxi = i
    return maxi
