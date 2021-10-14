#!/usr/bin/python3
"""
================
pascala triangle
================
"""


def pascal_triangle(n):
    """ pascal triangle function """

    mat = []

    for m in range(n):
        mat.append([])

    for i in range(n):
        for j in range(i + 1):
            if i == j or j == 0:
                mat[i].append(1)
            else:
                res = mat[i-1][j] + mat[i-1][j-1]
                mat[i].append(res)

    return mat
