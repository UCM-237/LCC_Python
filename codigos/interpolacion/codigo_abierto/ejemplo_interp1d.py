# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 16:55:04 2024
Ejemplo de uso de la función interp1d de Scipy
@author: abierto
"""
import numpy as np
from scipy.interpolate import interp1d
from matplotlib import pyplot as pl
x = np.array([ 1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.])
y = np.array([-1.8143451, 20.914356, 26.714303, 61.129501,\
              76.414728, 123.00032, 167.06809, 212.97832,\
              258.67911, 320.53422])
#dibujamos los puntos
pl.plot(x,y,'o')
#creamos unos puntos sobre los que interpolar
xi = np.arange(1.,10.,0.01)
#creamos la función interpoladora empleando inter1d
flin = interp1d(x,y,'linear')#puede omitirse linear el la opcion por defecto
#empleamos la funcion para obtener los valores de los puntos interpolados
yi = flin(xi)
pl.plot(xi,yi)

fnear = interp1d(x,y,'nearest')
yi = fnear(xi)
pl.plot(xi,yi)

fnext = interp1d(x,y,'next')
yi = fnext(xi)
pl.plot(xi,yi)
#and so on and so forth...