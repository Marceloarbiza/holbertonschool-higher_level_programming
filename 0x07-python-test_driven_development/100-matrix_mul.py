#!/usr/bin/python3
"""
    Multiplies two matrices
"""


def matrix_mul(m_a, m_b):
    """ In this function we must
        multiplie two matrices

        mAB x mBC = mAC
    """
    if isinstance(m_a, list) is False:
        raise TypeError("m_a must be a list")
    if isinstance(m_b, list) is False:
        raise TypeError("m_b must be a list")

    for la in m_a:
        if isinstance(la, list) is False:
            raise TypeError("m_a must be a list of lists")
    for lb in m_b:
        if isinstance(lb, list) is False:
            raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for la in m_a:
        for i in la:
            if type(i) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for lb in m_b:
        for j in lb:
            if type(j) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")

    lena = len(m_a[0])
    for a in m_a:
        if len(a) != lena:
            raise TypeError("each row of m_a must be of the same size")
        lena = len(a)

    lenb = len(m_b[0])
    for b in m_b:
        if len(b) != lenb:
            raise TypeError("each row of m_b must be of the same size")
        lenb = len(b)

    if lena != lenb:
        raise ValueError("m_a and m_b can't be multiplied")
    

