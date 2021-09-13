#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    leni = len(my_list) - 1
    tmp_list = my_list[:]

    if idx < 0:
        return tmp_list
    elif idx > leni:
        return tmp_list
    else:
        tmp_list[idx] = element
        return tmp_list
