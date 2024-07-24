#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 10:40:23 2024

@author: juan
A code to implement the Lagrange polynomial
"""
import numpy as np

def lagrang(x,y,x1):
    """
    Function to calculate the Lagrange interpolating polynomial at point x1
    
    Parameters
    ----------
    x : TYPE real np array
        DESCRIPTION. Table Values x to be interpolated 
    y : TYPE real np array
        DESCRIPTION. Table values y to be interpolated
    x1 : TYPE real
        DESCRIPTION. Point a which the polynomial is evaluated

    Returns
    -------
    y1 : TYPE real
        DESCRIPTION. Lagrange polynomial Valueat x1. y1 = PLagrange(x1) 

    """
    y1 = 0
    n = x.shape[0]
    for j in range(0,n):
        lj = 1
        for i in range(0,j):
            lj = lj*(x1-x[i])/(x[j]-x[i])
        for i in range(j+1,n):
            lj = lj*(x1-x[i])/(x[j]-x[i])
        y1 = y1 +lj*y[j]
    return(y1)

def langrmult(x,y,x1):
    """
    Takes the funtion lagrang and calculates the values of the Lagrange
    polinomial at any point in array x1

    Parameters
    ----------
    x : TYPE real np array
        DESCRIPTION. Table Values x to be interpolated 
    y : TYPE real np array
        DESCRIPTION. Table values y to be interpolated
    x1 : TYPE real
        DESCRIPTION. array  of point a which the polynomial is evaluated

    Returns
    -------
    y1 : TYPE real
        DESCRIPTION. Lagrange polynomial Valueat x1. y1 = PLagrange(x1)

    """
    yaux = [] #fast way to create an array same size as x 
    for i in x1:
        yaux.append(lagrang(x,y,i))
    y1 = np.array(yaux)
    return(y1)
    
       