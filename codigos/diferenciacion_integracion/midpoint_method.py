# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 16:10:09 2024
The Runge-Kutta midpoint method
@author: abierto
"""
import numpy as np
import matplotlib.pyplot as pl
def pmedio(fun,xa,a,b,h):
    """
    This funtion implements the second-order Runge-Kutta method
    better known as the midpoint method

    Parameters
    ----------
    fin : TYPE function
        DESCRIPTION. a funtion describing the initial value problem
        derivative to be integrate
    xa : TYPE numpy array
        DESCRIPTION. initial condition
    a : TYPE double
        DESCRIPTION. initial integratio point
    b : TYPE double 
        DESCRIPTION. final integration point
    h : TYPE double
        DESCRIPTION. integration step

    Returns
    -------
    x: TYPE numpy array 
       DESCRIPTION. solutions at points a, a+h, a+2h etc
    t. TYPE numpy array
       DESCRIPTION. times x has been computed at 
    """
    if a >= b:
        raise ValueError('I need an increasing interval')
    
    #to arrive to the final condition, we modify slighly the
    #integration step. First we calculate the aproximate number
    #of intervals between a and b of size h and round it towards
    #infinite.
    pt = int(np.ceil((b-a)/h))
    #then, we modify the integration step to acomodate at 
    #the rounded number of interval. This is, of course, not
    #necessary to implement the method, there are other
    #posibilities to deal with the integration step and
    #the limit b
    hft = (b-a)/pt
    t = np.arange(a,b+hft,hft)
    x = np.zeros([xa.shape[0],pt+1])
    x[:,0] = xa
    for i in range(1,pt+1):
        x[:,i] = x[:,i-1] + hft*fun(t[i-1]+hft/2,x[:,i-1]\
                 +hft*fun(t[i-1],x[:,i-1])/2)
    pl.plot(t,x.T)
    return(t,x)