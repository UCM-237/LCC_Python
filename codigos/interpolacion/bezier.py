# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 19:41:24 2024
This module defines a functions to generate Bezier Polynomials
bezier returns the value of the curve as a function of t
bezier_rc uses function bezier to obtain the values of the curve
y an array of point a draw the result
@author: abierto
"""
import numpy as np
import matplotlib.pyplot as pl
    

def bezier(p,t):
    """
    Calculates de value of a bezier curve with control points
    in the array p at value t

    Parameters
    ----------
    p : TYPE numpy array
        DESCRIPTION. Numpy array of dimension 2Xn where n is the
        number of control points. first row contains x coordinate 
        and second row contain y coordinate, the curve pass through
        the first a last control points
    t : TYPE 
        DESCRIPTION. Berstein's polynomial parameter t belongs 
        to [0,1]

    Returns
    -------
    ber : TYPE np.array 
          DESCRIPTION. ber[0] x coordinate of the bezier's curve 
          at t. ber[1] y coordinate of the bezier's curve at t

    """
    n = p.shape[1]
    num = np.arange(1,n).prod()
    #we firt calculate all factorial needed
    ftal = np.insert(np.arange(1.,n).cumprod(),0,1)
    ber = np.zeros(2)
    for i in range(n):
        f = num/ftal[i]/ftal[n-1-i]
        ber = ber + f*p[:,i]*(1-t)**(n-1-i)*t**i
    return(ber)

def bezier_sc(p,t):
    """
    This function use funtion bezier to reproduce the bezier curve
    with control point containing in p. 
    Parameters
    ----------
    p : TYPE numpy array
        DESCRIPTION. Numpy array of dimension 2Xn where n is the
        number of control points. first row contains x coordinate 
        and second row contain y coordinate, the curve pass through
        the first a last control points
    t : TYPE numpy array 
        DESCRIPTION. It should be an array of ordered values for
        parameter t. To reproduce de whole Bezier's curve use
        t = numpy.arange(0,1+step,step) the smaller step the smoother
        the result

    Returns
    -------
    pt : TYPE numpy array
         DESCRIPTION. a 2xm array with m the number of data in t
         first row containts the x coordinates at the values of t
         and second row the y coordinates at the values of t

    """
    pt = np.array([bezier(p,i) for i in t]).T
    pl.plot(p[0],p[1],'or')
    pl.plot(p[0],p[1],'-.')
    pl.plot(pt[0],pt[1])
    return(pt)

def bzeq(p,n,step):
    """
    Computes Bezier's curves of higher degree, equivalent to a
    given Bezier's curve

    Parameters
    ----------
    p : TYPE numpy array
        DESCRIPTION. 2xn array containing the control points of
        the Bezier's curve to be derivate. (each column a point) 
    n : TYPE integer 
        DESCRIPTION. Degree of the equivalent Bezier's, it should
        be greater than the number of points in p.
    step : TYPE double
        DESCRIPTION. a step to generate an ordered,  array which
        equispaciate values in [0,1]. 

    Returns 
    -------
    p : TYPE numpy array
        DESCRIPTION. 2x(n-1) array containing the control points
        of the equivalent Bezier's curve

    """
    c = p.shape[1]
    t = np.arange(0,1+step,step)
    bezier_sc(p, t) #draw the Bz curve
    if c < n:
        #adding one more control point and recalculating
        # the control points
        p = np.append(p,[[0],[0]],axis=1)
        pp =p.copy()
        for i in range(1,c+1):
            pp[:,i] = p[:,i-1]*i/(c) + (1 -i/(c))*p[:,i]
        #the function calls itself till the number of points
        #equals n
        p = bzeq(pp,n,step)
    # and it returns the control points. In the meanwhile it
    #has drawn all the equivalent curves with degrees between
    # c and n    
    return(p)

def dbez(p):
    """
    Compute a Bezier's . Curve derivative, defined by control 
    points in p. It also draw de odograph and the derivatives
    at some selected points and the Bezier's curve and
    the derivative, as tangents vector, as some selected points.

    Parameters
    ----------
    p : TYPE numpy array
        DESCRIPTION. Control points of the Bezier's curve we 
        wanna derivate.

    Returns 
    -------
    d : TYPE numpy array
        DESCRIPTION. Controls points of the derivative. 

    """
    grado = p.shape[1]-1
    d = np.zeros([2,grado])
    #compute the control points of the derivativa
    for i in range(grado):
        d[:,i] = (grado-1)*(p[:,i+1]-p[:,i])
    t = np.arange(0,1+0.01,0.01)
    #plot de odograph 
    pl.figure(1)
    v = bezier_sc(d, t)    
    pl.quiver(np.zeros(12),np.zeros(12),\
              v[0,::9],v[1,::9],\
              angles='xy', scale_units='xy', scale=1)
    
    #plot the curve and its derivative. (the escale of the 
    #vector is arbitrary)
    pl.figure(2)
    ptos = bezier_sc(p,t)
    pl.quiver(ptos[0,::9],ptos[1,::9],\
              v[0,::9],v[1,::9])
    pl.axis('equal')
    return(d)        