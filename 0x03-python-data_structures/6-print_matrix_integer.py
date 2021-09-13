#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        print("{}" .format((str(matrix[i])[1:-1]).translate({ord(","): None})))
