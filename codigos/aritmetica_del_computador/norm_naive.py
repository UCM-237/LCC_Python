#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Two functions to compute the Euclidean norm of a vector.
norma_naive overflows when the square of an element is larger than the
largest representable number; norma_robust scales the elements to avoid it.
@author: juan
"""

import numpy as np

def norma_naive(x):
    """
    Calculates the norm of a vector (naive version)
    Parameters
    ----------
    x : real vector (1D numpy array)
        input vector whose norm we want to get

    Returns
    -------
    m : real number
        the norm of the vector
    """
    m = 0.
    for e in x:
        m = m + e**2
    m = np.sqrt(m)
    return m

def norma_robust(x):
    """
    Calculates the norm of a vector, scaling its elements by the largest
    absolute value found so far, to avoid overflow and underflow
    Parameters
    ----------
    x : real vector (1D numpy array)
        input vector whose norm we want to get

    Returns
    -------
    m : real number
        the norm of the vector
    """
    if x.shape[0] == 1:
        return np.abs(x[0])
    mayor = 0.          # largest absolute value found so far
    mscalado = 0.       # sum of (x_i/mayor)**2 for the elements seen so far
    for e in x:
        if e == 0:
            continue
        modxi = np.abs(e)
        if mayor < modxi:
            # new largest element: rescale the accumulated sum
            mscalado = 1 + mscalado*(mayor/modxi)**2
            mayor = modxi
        else:
            mscalado = mscalado + (modxi/mayor)**2
    m = mayor*np.sqrt(mscalado)
    return m
