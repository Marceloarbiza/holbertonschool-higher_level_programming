#!/usr/bin/python3

def matrix_divided(matrix, div):

    if isinstance(matrix, list) is False:
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    for x in matrix:
        if len(x) == 0:
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    for m in matrix:
        if isinstance(m, list) is False:
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
        else:
            for i in m:
                if type(i) not in [int, float]:
                    raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    len0 = len(matrix[0])
    for le in matrix:
        if len(le) is not len0:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(i/div, 2) for i in m] for m in matrix]
