# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 11:08:42 2024
Euler's method for solving initial value problems
@author: abierto
"""
import numpy as np
import matplotlib.pyplot as pl

def euler(fun,xa,a,b,h):
    """
    This function solve numerically the problem dx/dt = f(t,x)
    form the intial condition xa along the interval [a,b] and
    using an integration step h

    Parameters
    ----------
    fun : TYPE function
        DESCRIPTION. it is the funtion that describe the differential
        equation to be solved it should be a funtion of t and x 
        f(t,x) also is there is not explicit dependence on t.
    xa : TYPE numpy array 
        DESCRIPTION. initial condition
    a : TYPE double
        DESCRIPTION. initial value of t
    b : TYPE double
        DESCRIPTION. final value of t
    h : TYPE double
        DESCRIPTION. integration step

    Returns
    -------
    x : TYPE numpy array
        DESCRIPTION. intial value dx/dt = f(x) solution at points
        a, a+h a+2h ... b
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
        x[:,i] = x[:,i-1] + hft*fun(t[i-1],x[:,i-1])
    pl.plot(t,x.T)
    return(t,x)
        
               