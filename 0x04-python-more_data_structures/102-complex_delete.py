#!/usr/bin/python3
def complex_delete(a_dictionary, val):
    list_Del = []
    for key, value in a_dictionary.items():
        if value == val:
            list_Del.append(key)

    for i in list_Del:
        del a_dictionary[i]

    return a_dictionary
