# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 11:01:10 2024
This script implemets some functions to compute Cubic spline
@author: abierto
"""
import numpy as np

def spcubic(x,y,xi):
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
    c : spline coeficients
    y1 : TYPE real
        DESCRIPTION. Lagrange polynomial Value at x1. y1 = lagrang(x1) 

    """
    l = x.shape[0] #number of data
    dy = np.zeros(l-1)
    h = dy.copy()

    for i in range(0,l-1):
        h[i] = x[i+1] - x[i] 
        dy[i] = y[i+1]-y[i]
    CSPp = np.zeros(l-2)
    b = CSPp.copy()
    for i in range(l-2):    
        CSPp[i] = 2*(h[i+1]+h[i]) #ppal diagonal
        b[i] = 6*(dy[i+1]/h[i+1]-dy[i]/h[i])
    #building the system matrix (a pro. would use a spare matrix here)
    CSP = np.diag(CSPp)+np.diag(h[1:-1],1)+np.diag(h[1:-1],-1)
    M = np.linalg.solve(CSP,b)
    M = np.insert(M,0,0)
    M= np.append(M,0)
    A = np.zeros(l-1)
    for i in range(l-2):
        A[i] = dy[i]/h[i] - (M[i+1]-M[i])*h[i]/6
        
    
        
    
    