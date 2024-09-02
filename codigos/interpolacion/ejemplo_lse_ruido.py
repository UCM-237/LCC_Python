# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 20:29:50 2024
Example of residual an precission of a lms fit.
Not to be distributed among our little, hairy and groovy students
@author: abierto
"""
import numpy as np
from matplotlib import pyplot as pl
from numpy.polynomial import Polynomial as py
#generamos unos puntos sobre un polinomio cubico
pl.close('all')
p = py.fromroots([1,3,8])
x = np.arange(10)
y = p(x)
#a ver que aspecto tienen
f0 = pl.figure(0)
pl.plot(x,y,'o')

#ahora le metemos un poco de ruidillo
ruidillo = 20*(np.random.default_rng().random(10)-0.5)

yr = y + ruidillo

pl.plot(x,yr,'+')

#vamos a calcular varias regresiones.
xi = np.arange(0,9,0.1)
#lineal
p1 = py.fit(x,yr,1)
p2 = py.fit(x,yr,2)
p3 = py.fit(x,yr,3)
p4 = py.fit(x,yr,4)

y1 = p1(x)
y2 = p2(x)
y3 = p3(x)
y4 = p4(x)

y1i = p1(xi)
y2i = p2(xi)
y3i = p3(xi)
y4i = p4(xi)

res1 = yr - y1
res2 = yr - y2
res3 = yr - y3
res4 = yr - y4

#graficos lineal
f1 = pl.figure(1)
ax1 = pl.subplot(2,1,1)
pl.plot(x,yr,'o')
pl.plot(xi,y1i)
pl.legend(['data','linear'])
ax2 = pl.subplot(2,1,2)
pl.bar(x,res1)
pl.title('residuals')

#graficos quadratic
f2 = pl.figure(2)
ax1 = pl.subplot(2,1,1)
pl.plot(x,yr,'o')
pl.plot(xi,y2i)
pl.legend(['data','quadratic'])
ax2 = pl.subplot(2,1,2)
pl.bar(x,res2)
pl.title('residuals')

#graficos cubic
f2 = pl.figure(3)
ax1 = pl.subplot(2,1,1)
pl.plot(x,yr,'o')
pl.plot(xi,y3i)
pl.legend(['data','cubic'])
ax2 = pl.subplot(2,1,2)
pl.bar(x,res3)
pl.title('residuals')

#graficos 4th degree
f2 = pl.figure(4)
ax1 = pl.subplot(2,1,1)
pl.plot(x,yr,'o')
pl.plot(xi,y4i)
pl.legend(['data','linear'])
ax2 = pl.subplot(2,1,2)
pl.bar(x,res4)
pl.title('residuals')