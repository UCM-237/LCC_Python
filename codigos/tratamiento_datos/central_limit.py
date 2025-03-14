#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 16:13:56 2025
EStudiamos el teorema central del límite, generando números aleatorios
We study the centrar limit theorem using random numbers
@author: juan
"""

import numpy as np
import matplotlib.pyplot as pl
#creamos un generador de números aleatorios,
#create a random generator
#usamos una semilla para que se pueda reproducir tal cual
#we use a seed, so the secuence of random number is alwaus the same
gen_num = np.random.default_rng(1000)

#generamos un ,millón de vectores, formados por número aletorios distribuidos
#en el intervalo [-1,1). calculamos el valor medio de los 10 elementos de
#cada vector y guardamos los resultados en un nuevo vector.
#esto puede llevar un rato
#We generate a millon of vectors built from random number distributed in the
#interval [-1,1). We calculte the mean of the vector elements and save the
#result in a new vector.
#this could take time
media10 = np.zeros(1000000) #vector para guardar las medias/vector forsaving the means
for i in range(1000000):
    media10[i] = np.mean(2*gen_num.random([10,1])-1)
    
#repetimos el cálculo pero ahora con vectores de 100 elementos
#repeat the computing but now we take vectors of 100 elements
media100 = np.zeros(1000000) #vector para guardar las medias
for i in range(1000000):
    media100[i] = np.mean(2*gen_num.random([100,1])-1)

#creamos las distribuciones a las que pertenecen nuestras medias
#we create the distributions our means belong to
def normal(x,mu,s2):
    y = np.exp(-(x-mu)**2/2/s2)/np.sqrt(2*np.pi*s2)
    return(y)
#Para medias obtenidas de 10 medidas
#for means getting from 10 data
d10 = np.array([i for i in  np.arange(-0.9,0.9,0.01)])
#para medias obtenidas de 100 medidas
#for means getting from 100 data
d100 = np.array([i for i in  np.arange(-0.9,0.9,0.01)])   
y10 = normal(d10,0,1./30)
y100 = normal(d100,0,1./300)

#creamos histogramas de 50 barras de la misma anchura
#buiding a histogram of 50 bars with the same width
counts10, bins10 = np.histogram(media10,50)
#calculamos el ancho de las barras para normalizar el histograma y así
#poder comparar con la distribución a la que pertenece

#computing the width of the bars to normalizate the histogram and so can
#compare it with the distribution it belongs to
anch10 = (max(media10)-min(media10))/50
#normalizamos la altura de las barras
#normalizing the bars height
cn10 = counts10/1000000/anch10

#same story for the other distrbutions
counts100, bins100 = np.histogram(media100,50)
anch100 = (max(media100)-min(media100))/50
cn100 = counts100/1000000/anch100

#ploting de results.
ax1 = pl.subplot(1,2,1)
ax1.hist(bins10[:-1],bins10,weights= cn10)
ax1.plot(d10,y10)
pl.xlabel('x')
pl.ylabel('Probabilidad')
ax2 = pl.subplot(1,2,2)
ax2.hist(bins100[:-1],bins100,weights= cn100)
ax2.plot(d100,y100)
pl.xlabel('x')
pl.ylabel('Probabilidad')

