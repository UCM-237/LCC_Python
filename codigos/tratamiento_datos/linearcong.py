#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:51:02 2025
Generados aleatorios linear congruential
@author: juan
"""
import matplotlib.pyplot as pl
def linear_con(i0,a,c,m,l):
    """
    

    Parameters
    ----------
    i0 : TYPE integer
        DESCRIPTION. seed /semilla
    a : TYPE integer
        DESCRIPTION. multiplier 0 <= a < m
    c : TYPE integer
        DESCRIPTION. Increment 0 <= c < m
    m : TYPE int
        DESCRIPTION. Module > I0 (the larger the better)
    l : TYPE int
        DESCRIPTION. number of elements in the random sequence 

    Returns
    -------
    secuencia : TYPE List of double 0<=secuencia[i]<=1
        DESCRIPTION. Sequence o l pseudo-random numbers

    """
    secuencia=[]
    for i in range(1,l):
        i0 = (i0*a+c)%m
        secuencia.append(i0/m)
    return secuencia
#ejemplo/example
sec = linear_con(1000,3,10,100000,1000)
pl.plot(sec)