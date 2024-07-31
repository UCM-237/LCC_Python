#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 15:22:01 2024
This file define two funtion. one to calculate the divided differences 
polynomial coefficients and the second one to evaluate the divided differences
polynomial any point
@author: juan
"""
import numpy as np
import matplotlib.pyplot as pl
def difdiv(x,y):
    """
    This functions computes the coefficient of a the divided differences 
    polynomial using thw data arrays x,y 

    Parameters
    ----------
    x : TYPE double
        DESCRIPTION. numpy array with data x
    y : TYPE double
        DESCRIPTION. numpy array with data y

    Returns
    -------
    a : TYPE double
        DESCRIPTION: coefficientes of the polynomial
        p_n(x)=a_0+(x-x_0)a_1+(x-x_0)(x-x_1)a_2+...
        ...+(x-x_0)(x-x_1)...(x-x_{n-2})(x-x_{n-1})a_n
    """
    n = x.shape[0] #number of data
    #we use the y variable to inisialise the vector of coefficients
    a = y.copy() #warning I need to copy to avoid overwrite the values of y
    #we must compute n differences 
    for j in range(1,n): #start in 1 we alredy have the order zero differences    
        for i in range(j,n):
            a[i] = (a[i]-y[i-1])/(x[i]-x[i-j])
        y = a.copy()
    return(a)

def evdif(a,x,xi):
    """
    Evaluates the divided diferences polynomial from points x and coefficients
    y. 

    Parameters
    ----------
    y : TYPE double
        DESCRIPTION. numpu arrray with divided differences polynomial coefficients
    x : TYPE double
        DESCRIPTION. numpy array with x data from the table to be interpolated
    xi : TYPE double
        DESCRIPTION. point to calculate the polynomial at. It can be also an array

    Returns 
    -------
    y1: TYPE: double
        DESCRIPTION: computed value of the polynomial at x1
    """
    n = a.shape[0]
    yi = a[0] #copy the first coefficient into the result 
    for k in range(1,n):
        #product of binomials to be multiplied for the coefficients
        binprod = 1
        for j in range(k):
            binprod = binprod*(xi-x[j])
        yi = yi +a[k]*binprod
    return(yi)