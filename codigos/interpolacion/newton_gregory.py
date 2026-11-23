# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 20:12:49 2024
A gruby version of Newton-Gregory polynomial 
@author: abierto
"""
import numpy as np
from dif_div import evdif
def newgre(x,y,x1=0):
    """
    

    Parameters
    ----------
    x : TYPE numpy array of data
        DESCRIPTION.
    y : TYPE numpy array of data 
        DESCRIPTION.
    x1 : TYPE a point to calculate the value the polynomial
         takes
        DESCRIPTION.
        This function takes a data set, represented by the
        x and y array and obtain the corresponding 
        newton-gregory polynomial.Besides it calculates the
        value of the polypolimial at the point x1. if no x1
        value is supplied then it takes x1 =0 by default.
        The program returns the polynomial coeficients and
        the value calculated at point x1

    Returns
    -------
    a : TYPE numpy array of polynomial coeficients
        DESCRIPTION.
    y1: TYPE real value
        DESCRIPTION. The value the polynomial takes at x1

    """
    n = x.shape[0]
    h = x[1] -x[0]
    # The method only works for equispaced data in increasing order
    if h <= 0 or not np.allclose(np.diff(x), h):
        raise ValueError('x must be equispaced and in increasing order')
    a = y.astype(float) #we start the coefficient with the 0-order
               #differences, i.e. y values. A float copy: with integer
               #data, y.copy() would truncate the divisions
    #here start the loop to calculate the differences
    for j in range(1,n):
        #for each iteration we calculate the differences
        #of higher order. But we only need the first difference. So we restart
        #the inner loop in the value j of the outer one
        prev = a.copy() # differences of order j-1
        for i in range(j,n):
            #now it is enough to divide for the distance h betwwen x point 
            #multiplied by order j of the diference
            a[i] = (prev[i]-prev[i-1])/(j*h)
    #now we calculate the value(s) of the polynomial using the
    #function built to evaluate divided diferences polynomials 
    y1 = evdif(a,x,x1)
    return(a,y1)