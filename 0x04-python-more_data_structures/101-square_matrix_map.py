#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_matrix = list(map(lambda li: list(map(lambda num: num**2, li)), matrix))
    return new_matrix
