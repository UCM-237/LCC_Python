# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 16:21:54 2024

@author: abierto
"""
import numpy as np
from matplotlib import pyplot as pl
def integra(fun,met,inter,dib=False):
    """
    function numerical integration, using trapezium, Simpson's
    1/3 or Simpson 3/8 methods

    Parameters
    ----------
    fun : TYPE function
        DESCRIPTION. Function to be integrated
    met : TYPE char array 
        DESCRIPTION. method should be one of 'trap' 'simpson' 
        or 'simpson38'
    inter : TYPE array [a,b]
        DESCRIPTION. integration interval limits
    dib : TYPE logical
        DESCRIPTION. yes : draw the results no: skip the drawing
        
    Returns 
    -------
    intg: TYPE double
        DESCRIPTION. Integral value
        f1 = fun(inter[1])
        h = inter[1] - inter[0]

    """
    if met == 'trap':
        f0 = fun(inter[0])
        f1 = fun(inter[1])
        h = inter[1] - inter[0]
        intg = h*(f0+f1)/2
        if dib:
            x = np.linspace(inter[0],inter[1],100)
            y = np.array([fun(i) for i in x])
            ypol = f0 + (x - inter[0])*(f1-f0)/h
            pl.fill_between(x,ypol,\
                            where=(inter[0]<=x)&(x<=inter[1]))
            pl.plot(x,y,'b')
    elif met == 'simpson':
        pmedio = (inter[1] + inter[0])/2
        f0 = fun(inter[0])
        f1 = fun(pmedio)
        f2 = fun(inter[1])
        h =  (inter[1] - inter[0])/2
        intg = h*(f0+4*f1+f2)/3
        if dib:
            x = np.linspace(inter[0],inter[1],100)
            y = np.array([fun(i) for i in x])
            ypol = f0+(x-inter[0])*(f1-f0)/h\
                +(x-inter[0])*(x-pmedio)*(f2-2*f1+f0)/(2*h**2)
            pl.fill_between(x,ypol,\
                            where=(inter[0]<=x)&(x<=inter[1]))
            pl.plot(x,ypol,'k')
            pl.plot(x,y,'b')
    elif met == 'simpson38':
        inter = np.linspace(inter[0],inter[1],4)
        f = np.array([fun(i) for i in inter])
        h = inter[1]-inter[0]
        intg = 3*h*(f[0]+3*f[1]+3*f[2]+f[3])/8
        if dib:
            x = np.linspace(inter[0],inter[3],100)
            y = np.array([fun(i) for i in x])
            ypol = f[0]+(x-inter[0])*(f[1]-f[0])/h\
                   +(x-inter[0])*(x-inter[1])\
                   *(f[2]-2*f[1]+f[0])/(2*h**2)\
                   +(x-inter[0])*(x-inter[1])*(x-inter[2])\
                   *(f[3]-3*f[2]+3*f[1]-f[0])/(6*h**3)    
            pl.fill_between(x,ypol,\
                          where=(inter[0]<=x)&(x<=inter[3]))
            pl.plot(x,ypol,'k')
            pl.plot(x,y,'b')
    return(intg)

def trocea(fun,met,inter,div,dib=False):
    """
    This funtion divide a interval into the number of subintervals indicate
    by div and calls function integra to obtain the integral in 
    any subinterval. Eventually sums all results to compute the
    integral over the whole interval

    Parameters
    ----------
    fun : TYPE function
        DESCRIPTION. function to be integrate
    met : TYPE character string 
        DESCRIPTION. Method it should be one of 'trap' 'simpson' 
        or 'simpson38'can be 'trap', 
    inter : TYPE array or list 
        DESCRIPTION. limits for the integration interval [a,b]
    div : TYPE integer
        DESCRIPTION. Number of subintervals
    dib : TYPE bool
        DESCRIPTION. True draw the result False does not draw

    Returns
    -------
    total : TYPE double
          DSCRIPTION Definite integral value of fun in inter

    """
    tramos = np.linspace(inter[0],inter[1],div+1)
    total = 0
    for i in np.arange(div):
        int = integra(fun,met,[tramos[i],tramos[i+1]],dib)
        total = total + int
    return(total)
