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


