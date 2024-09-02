#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 15:02:07 2024


@author: juan
"""
import numpy as np
from matplotlib import pyplot as pl
def taylorln(x,n):
    """
    Esta función aproxima el valor del logaritmo natural de un numero
    empleando para ello un polinomio de Taylor de grado n desarrollado en 
    torno a x=1. Las variables de entrada son: x, valor para el que se desea 
    calcular el logaritmo. n Grado del polinomio que se empleará en el 
     cálculo. La variable de salida y es el logaritmo de x. 
    This fuction computes (approx) the value of the natural logarithm for a number 
    using a degree n Taylor's polynomial, at x0=1. input variables are: x, value to
    calculate its logarithm. n degree of the polynomial useto aporaches the log.
    the funtion returns the locarithm computed. 

    Parameters
    ----------
    x : Real
        
    n : int
        Taylor's polinomial Degree 

    Returns
    -------
    y : real
        log(x)

    """
    y = 0
    for i in range(1,n+1):
        y = y+(-1)**(i+1)*(x-1)**i/i
        
    return(y)
    

def taylorcum(fun,n,x):
    """
    

    Parameters
    ----------
    fun : takes the taylor series of degree n, described in input function fun
          and calculates and draws the result for an array of points, x 
        DESCRIPTION.
    n : TYPE int
        DESCRIPTION.
        Taylor's polynomial degree'
    x : TYPE array of real numbers
        DESCRIPTION. point to calculate the Taylor series

    Returns 
    -------
    y : Type real
        DESCRIPTION: array of values computed 

    """
    
    y =np.array([fun(i,n) for i in x])
    pl.plot(x,y)