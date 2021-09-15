#!/usr/bin/puthon3
def uniq_add(my_list=[]):
    res = sum(dict.fromkeys(my_list))
    return res
