#!/usr/bin/python3
def roman_to_int(roman_string):

    list_num = []
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0

    if type(roman_string) is not str or roman_string is None:
        return 0

    for i in roman_string:
        list_num.append(roman[i])

    max_value = max(list_num)
    max_index = list_num.index(max_value)

    if max_index > 0:
        list_num.reverse()
        res = list_num[0]
        for i in range(1, len(list_num)):
            res -= list_num[i]
    else:
        res = sum(list_num)

    return res
