#!/usr/bin/python3
def max_integer(my_list=[]):
    maxi = 0
    bol = True
    if bool(my_list) == False:
        return None
    else:
        for i in my_list:
            if maxi < i:
                maxi = i
    return maxi
