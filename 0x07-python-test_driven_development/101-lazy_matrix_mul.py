#!/usr/bin/python3
"""
    multiplies 2 matrices with numpy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
        This function must multiply
        two matrices in a lazy mode
    """

    return np.dot(m_a, m_b)
