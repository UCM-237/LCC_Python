# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 20:15:18 2024
Function to obtain the least squared error polynomial from a dataset
@author: abierto
"""
import numpy as np
def lse(x,y,n,w='none'):
    """
    This function compute the least squared error polynomial of
    degree n from a set of data x,y. Optionally it can use a
    set of weights to perform the computation
    Parameters
    ----------
    x : TYPE numpy array
        DESCRIPTION. x data to be fitted
    y : TYPE numpy array 
        DESCRIPTION. y data to be fitted
    n : TYPE integer
        DESCRIPTION. Polynomial degree
    w : TYPE numpy array with the same length than x and y
        DESCRIPTION.

    Returns
    -------
    a: TYPE numpy array 
       DESCRITION.  polynomial coefficients in increasing powers
           a[0]+a[1]x+a[2]x**2+...+a[n]x**n

    """
    m = x.shape[0] 
    #first we check that we have enought points
    if m < n:
        raise Warning('the degree is greater than the number of data')
    #if there is no weight array generate an arry of ones
    if type(w)==str:
        w = np.ones(m)
    #we build the s elements of the system coefficient matrix
    n = n+1 # for degree n I need n+1 coeficientes
    s = np.zeros(2*n)
    for j in range(2*n):
        for i in range(m):
            s[j] = s[j] + w[i]*x[i]**j
    c = np.zeros(n)
    for j in range(n):
        for i in range(m):
            c[j] = c[j] + w[i]*x[i]**j*y[i]
    A = np.zeros([n,n])
    for i in range(n):
        for j in range(n):
            A[i,j] = s[i+j]
    a =np.linalg.solve(A,c)
    return(a)

