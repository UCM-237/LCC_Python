#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 16:56:09 2024

@author: lia

LCC in Python.
Root finding methods
"""

import numpy as np
import matplotlib.pyplot as plt


def f_prueba(x):
    y=np.exp(x)-x*x
    return y

def biseccion(f,a,b,tol,itmax):
    ''' Bisection Method to compute roots
    f: function from which the roots are to be calculated inside [a,b]
    tol: desired tolerance
    itmax: maximum number of iterations
    '''
    nit=0
    r=0
    if f(a)*f(b)>0:
        '''the conditions of bozano's theorem are not fulfilled'''
        return
    while np.abs(a-b)>tol or nit<itmax:
        c=(a+b)*0.5
        if f(c)*f(a)<0:
            b=c
        else:
            a=c
        nit+=1
    r=c
    error=np.abs(f(c))
    return r,error,nit


