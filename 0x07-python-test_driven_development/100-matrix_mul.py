#!/usr/bin/python3
"""
    Multiplies two matrices
"""


def matrix_mul(m_a, m_b):
    """ In this function we must
        multiplie two matrices
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
        if [(type(i) is not int or type(i) is not float) for i in la]:
            raise TypeError("m_a should contain only integers or floats")
