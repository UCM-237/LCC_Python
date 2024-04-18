#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 16:56:09 2024

@author: lia

LCC in Python.
Root finding methods
"""

import numpy as np



def f_prueba(x):
    y=np.exp(x)-x*x
    return y

def df_prueba(x):
    y=np.exp(x)-2*x
    return y


def biseccion(f,a,b,tol,itmax):
    ''' Bisection Method to compute roots
    f: function from which the roots are to be calculated inside [a,b]
    tol: desired tolerance
    itmax: maximum number of iterations
    '''
    nit=0
    r=0
    if f(a)*f(b)>0:
        '''the conditions of bozano's theorem are not fulfilled'''
        return
    c=(a+b)*0.5
    while np.abs(f(c))>tol and nit<itmax:
        c=(a+b)*0.5
        if f(c)*f(a)<0:
            b=c
        else:
            a=c
        nit+=1
    r=c
    error=np.abs(f(c))
    return r,error,nit


def regula_falsi(f,a,b,tol,itmax):
    ''' False Position Method to compute roots
    f: function from which the roots are to be calculated inside [a,b]
    tol: desired tolerance
    itmax: maximum number of iterations
    '''
    nit=0
    r=0
    if f(a)*f(b)>0:
        '''the conditions of bozano's theorem are not fulfilled'''
        return
    c=b-(f(b)/(f(b)-f(a)))*(b-a)
    while np.abs(f(c))>tol and nit<itmax:
        c=b-(f(b)/(f(b)-f(a)))*(b-a)
        if f(c)*f(a)<0:
            b=c
        else:
            a=c
        nit+=1
    r=c
    error=np.abs(f(c))
    return r,error,nit

def newton_raphson(f,df,x0,tol,itmax):
    ''' Newton Raphson Method to compute roots
    f: function from which the roots are to be calculated
    df: function derivative
    x0: initial point
    tol: desired tolerance
    itmax: maximum number of iterations
    Returns: root, error and number of iterations
    '''
    nit=0
    while np.fabs(f(x0))> tol and nit <itmax:
        
        if np.fabs(df(x0))<0.000001:
            return x0,np.fabs(f(x0)),nit
        x0=x0-f(x0)/df(x0)
        nit+=1
    r=x0
    error=np.fabs(f(x0))
    return r,error,nit

def secant(f,x0,x1,tol,itmax):
    ''' Secant Method to compute roots
    f: function from which the roots are to be calculated
    x0: first point
    x1: second point
    tol: desired tolerance
    itmax: maximum number of iterations
    Returns: root, error and number of iterations
    '''
    nit=0
    x=x1-(f(x1)/(f(x1)-f(x0)))*(x1-x0)
    while np.fabs(f(x)) > tol and nit <itmax:
        x0=x1
        x1=x
        x=x1-(f(x1)/(f(x1)-f(x0)))*(x1-x0)
        nit+=1
    r=x
    error=np.fabs(f(x0))
    return r,error,nit

def biseccion_max(f,a,b):
    ''' Bisection Method to compute roots at highest precision
    f: function from which the roots are to be calculated inside [a,b]
    '''
    nit=0
    r=0
    if f(a)*f(b)>0:
        '''the conditions of bozano's theorem are not fulfilled'''
        return
    c=(a+b)*0.5
    while np.abs(b-a)>=np.abs(np.spacing(a)):
        c=(a+b)*0.5
        if f(c)*f(a)<0:
            b=c
        else:
            a=c
        nit+=1
        print(np.abs(b-a),"\t",np.spacing(a))
    r=c
    error=np.abs(f(c))

    return r,error,nit
