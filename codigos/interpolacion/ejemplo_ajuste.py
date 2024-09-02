# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 16:00:12 2024
Example of least squares fit using the numpy.polynomial class Polynomial
@author: abierto
"""
import numpy as np
from numpy.polynomial import Polynomial as py
from matplotlib import pyplot as pl
#we import the function included above to compare the result
#with the numpy.polynomial function
from minimos_cuadrados import lse
 
#define a data set to play with
x = np.array([ 1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.])
y = np.array([-1.8143451, 20.914356, 26.714303, 61.129501,\
              350.414728, 123.00032, 167.06809, 212.97832,\
              258.67911, 320.53422])
    
p3 = py.fit(x,y,3) #we are not including weight
#we get the polynomial coefficients just to see them
a = p3.convert().coef

#a set of point to evaluate the polynomial
xi = np.arange(1.,10.,0.01)

yi = p3(xi)

#point y[4] (see graphics bellow) apears to be an outlayer we can
#use weights to atenuate its influence
w = np.ones(x.shape[0])
w[4] = 0.5 #we reduce the weight of the outlayer
p3w = py.fit(x,y,3,w=w)
yiw = p3w(xi)

################################################################
#we repeate the calculation using our own funtion lse 
################################################################
an = lse(x,y,3)
p = py(an) #we create a polynomial object using the coeficients
yin = p(xi)
#repeat the computing using the weight
aw = lse(x,y,3,w)
pw = py(aw)
yinw = pw(xi)

#drawing the results to compare
ax1 = pl.subplot(2,1,1)
pl.plot(x,y,'o')
pl.plot(xi,yi)
pl.plot(xi,yiw)
ax1.legend(['Data','Polynomial.fit',\
            'Polynomial.fit (weights)'])
ax2 = pl.subplot(2,1,2)
pl.plot(x,y,'o')
pl.plot(xi,yin)
pl.plot(xi,yinw)
ax2.legend(['Data','lse','lse (weights)'])