#!/usr/bin/python3
def roman_to_int(roman_string):

    list_num = []
    tmp_list = []
    prim = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    res2 = 0
    if type(roman_string) is not str or roman_string is None:
        return 0

    for i in roman_string:
        list_num.append(roman[i])
    
    max_value = max(list_num)
    max_index = list_num.index(max_value)

    if max_index == 0:
        
        tmp_list = list_num[:]
        prim = list_num[0]
        list_num.pop(0)
        mv2 = max(tmp_list)
        mi2 = tmp_list.index(mv2)

        if mi2 > 0:
            res = list_num[0]
            tmp_list.reverse()
            res2 = tmp_list[0]
            for h in range(1, len(tmp_list)):
                res2 -= tmp_list[h]

            res = res + prim + res2
        else:
            res = sum(list_num)
            res = prim + res
    
    if max_index > 0:
        list_num.reverse()
        res = list_num[0]
        for i in range(1, len(list_num)):
            res -= list_num[i]
    
    
    return res
