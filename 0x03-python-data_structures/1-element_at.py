#!/usr/bin/python3
def element_at(my_list, idx):
    leni = len(my_list) - 1
    if idx < 0:
        return None
    elif idx > leni:
        return None
    else:
        return my_list[idx]
