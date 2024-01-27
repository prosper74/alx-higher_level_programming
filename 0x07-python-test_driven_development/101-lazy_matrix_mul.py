#!/usr/bin/python3
"""
The module is part of the Python test driven development
This module contains one function: lazy_matrix_mul
The function multiplies 2 matrices by using the module NumPy
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    :param m_a: the first matrix.
    :param m_b: the second matrix.
    Return the multiplication of two matrices.
    """

    return (np.matmul(m_a, m_b))
