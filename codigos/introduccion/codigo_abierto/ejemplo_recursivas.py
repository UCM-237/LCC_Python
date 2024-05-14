#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 12:38:14 2024

@author: juan
"""

def fibonacci(n):
    """
    Parameters
    ----------
    n : TYPE integer
        DESCRIPTION. n is the fibonacci series term whose value we whant to 
        calculate
    n: es el término de la serie de fibonacci cuyo valor queremos calcular
        
    Returns 
    -------
    s : TYPE integer
        DESCRIPTION the value of fibonacci series term n

    """
    if n < 2:
        #the value of the term is n itself
        s = n
    else:
        s = fibonacci(n-1)+fibonacci(n-2)
    return(s)


def fibo_series(n):
    """
    Parameters
    ----------
    n : TYPE integer
        DESCRIPTION. Last number of the series whe want to build

    Returns
    -------
    Fs: List with the n first fibonacci series  terms.

    """
    Fs = [fibonacci(i) for i in range(n)]
    return(Fs)    