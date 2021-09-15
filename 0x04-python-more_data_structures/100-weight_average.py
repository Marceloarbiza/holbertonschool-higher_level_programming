#!/usr/bin/python3
def weight_average(my_list=[]):
    producto = 1
    suma = 0
    divisor = 0
    res = 0
    if my_list == []:
        return 0

    for i in my_list:
        producto = 1
        divisor += i[1]
        for j in i:
            producto *= j
        suma += producto

    res = suma / divisor
    return res
