# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 20:10:34 2024
Ejemplo de uso de los splines cubicos
@author: abierto
"""
import numpy as np
import matplotlib.pyplot as pl
from cubic_spline import spcubic, evspc

data = np.loadtxt('interpolacion.txt')
x = data[0,:]
y = data[1,:]        
M,A,B,C,h = spcubic(x,y)
xi = np.arange(1,10,0.01)
l = xi.shape[0]
yi =np.zeros(l)
for i in range(l):
    yi[i] = evspc(M,A,B,x,xi[i])
pl.plot(x,y,'o')
pl.plot(xi,yi)
