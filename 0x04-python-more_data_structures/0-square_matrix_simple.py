#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    twoDimList = []
    computeList = []
    for i in matrix:
        computeList = [n**2 for n in i]
        twoDimList.append(computeList)

    return twoDimList
