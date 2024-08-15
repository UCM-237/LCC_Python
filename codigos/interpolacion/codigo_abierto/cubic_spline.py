# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 11:01:10 2024
This script implemets some functions to compute Cubic spline
@author: abierto
"""
import numpy as np

def spcubic(x,y):
    """
    Function to calculate the spline coefficients
    Parameters
    ----------
    x : TYPE real np array
        DESCRIPTION. Table Values x to be interpolated 
    y : TYPE real np array
        DESCRIPTION. Table values y to be interpolated
    Returns
    -------
    h: Type array of diferecences betwee x consecutive data
    M,A,B: arrays with coefficientes for the polinomial that
           that compose the spline expressed as differences
           (see manual)
    C : TYPE numpy array size [I,4]
        I->intervals i.e number of data - 1
        4->Each 3-degree polinomial has 4 coefficients
        DESCRIPTION.spline coeficients in standard polynomial representation
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
    B = np.zeros(l-1)
    for i in range(l-1):
        A[i] = dy[i]/h[i] - (M[i+1]-M[i])*h[i]/6
        B[i]=y[i]-M[i]*h[i]**2/6
    C = np.zeros([l-1,4])
    for i in range(l-1):
        C[i,0]=y[i];
        C[i,1]=dy[i]/h[i]-M[i]*h[i]/3-M[i+1]*h[i]/6;
        C[i,2]=M[i]/2;
        C[i,3]=(M[i+1]-M[i])/(6*h[i]);
    return M,A,B,C,h  
    
def evspc(M,A,B,x,xi):
    """
    This function calculates the value of a interpolating spline in point xi
    
    Parameters
    ----------
    M : TYPE nummpy array
        DESCRIPTION. Coefficients M of the spline
    A : TYPE numpy array cofficients A of the spline
        DESCRIPTION.
    B : TYPE
        DESCRIPTION.
    x : TYPE numpy array
        DESCRIPTION. x data of the datatable interpolated
    xi : TYPE double 
        DESCRIPTION. point to calculate the spline value

    Returns
    -------
    yi : TYPE double
        DESCRIPTION. value calculate for the spline yi =s(xi) 

    """
    l = x.shape[0]
    h = np.zeros(l-1)
    for i in range(0,l-1):
        h[i] = x[i+1] - x[i]
    j = 0
    while xi > x[j]:
        j = j+1
    if j > l - 1:
       j = l - 1
    elif j < 1:
        j = 1
    yi=-M[j-1]*(xi-x[j])**3/(6*h[j-1])+ M[j]*(xi-x[j-1])**3/(6*h[j-1])\
        +A[j-1]*(xi-x[j-1])+B[j-1]
    return yi
