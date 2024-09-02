#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 14:43:50 2024
This 
@author: juan
"""

import numpy as np

def norma_naive(x):
    """
    This program (naive) calculates the norm of a vector
    Parameters
    ----------
    x : TYPE Real Vector
        DESCRIPTION. imput vector  whose norm we wamma get

    Returns
    -------
    m: Type Real number
       Description. The vector norm 
    """
    
    
    m = 0. 
    for e in x:
        m = m +e**2
        
    m =np.sqrt(m)
    return m

def norma_robust(x):
       """
       This program calculates the norm of a vector
       Parameters
       ----------
       x : TYPE Real Vector
           DESCRIPTION. imput vector  whose norm we wamma get

       Returns
       -------
       m: Type Real number
          Description. The vector norm 
       """ 
       l =x.shape[0]
       if l==1:
           m = np.abs(x[0])
       else:
           mayor  = 0
           mscalado = -1
           for e in x:
               if e == 0:
                   continue
               modxi = np.abs(e)
               if mayor<modxi:
                   mscalado = 1 + mscalado*(mayor/modxi)**2
                   mayor = modxi
               else:
                   mscalado = mscalado+(modxi/mayor)**2
               m = mayor*np.sqrt(mscalado)
       return m
               