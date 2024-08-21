# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 20:16:17 2024

@author: abierto
"""
import numpy as np
import matplotlib.pyplot as pl
from Euler_method import euler

def amortiguador(t,y):
    """
    Defines the set of differetial equations for a damping
    oscilator 

    Parameters
    ----------
    t : TYPE double 
        DESCRIPTION. time
    y : TYPE numpy array
        DESCRIPTION. y[0] ->> position
                     y[1] ->> velocity

    Returns
    -------
    dydt : TYPE numpy arra
           DESCRIPTION. dydt[0] ->> velocity
                        dydt[1] ->> acceleration
    
    """
    g = 9.8 #gravity accel.
    k = 100. #spring constant
    m = 2.  #mass
    mu = 0.5 #friction constant
    dydt = np.zeros(2) 
    dydt[0]=y[1]
    dydt[1]=g-(k/m)*y[0]-(mu/m)*y[1];
    return(dydt)

yini = np.array([0,0])
pl.figure(1)
euler(amortiguador,yini,0,50,0.01)
pl.xlabel('t(s.)')
pl.ylabel('(-)')
pl.title('Amortiguador k= 100, mu = 0.5, m = 2, step/paso = 0.01')
pl.legend(['v m/s', 'y m'])
