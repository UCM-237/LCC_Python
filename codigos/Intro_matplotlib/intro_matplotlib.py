#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 16:19:12 2024

@author: lia
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as manimation

'''
x=np.array([0, 2, -1, -2])
y=np.array([0, 3, 2, -4])
plt.subplot(2,2,1)
plt.plot(x,y,':')
plt.subplot(2,2,2)
plt.plot(x,y,'.r')
plt.subplot(2,2,3)
plt.plot(x,y,'-^k')
plt.subplot(2,2,4)
plt.plot(x,y,'s:m')

t1 = np.arange(0.0, 5.0, 0.1)
plt.subplot(2,1,1)
plt.plot(t1,np.cos(t1),'r.-')
plt.subplot(2,1,2)
plt.plot(t1,np.sin(t1),'b.-')

plt.figure()
t=np.arange(0.0,5,0.01)
y=np.exp(-t) * np.cos(2*np.pi*t)
plt.plot(t,y)
plt.title("Evolución de un sistema amortiguado")
plt.xlabel('t(s)')
plt.ylabel('x(m)')
plt.text(2.5,0.8,'$x=e^{-t}\cos(2\pi \cdot t)$')
'''
''' Escalas
x=np.linspace(0,10,100)
y=np.exp(x)
plt.figure()

plt.subplot(3,1,1)
plt.plot(x,y)
plt.grid()
plt.xlabel("Escala lineal")
plt.ylabel("Escala lineal")
plt.title("$y=e^x$")

plt.subplot(3,1,2)  
plt.plot(x,y)
plt.yscale('log')
plt.xlabel("Escala lineal")
plt.ylabel("Escala logarítmica")
plt.grid()


plt.subplot(3,1,3)  
plt.plot(x,y)
plt.xscale('log')
plt.yscale('log')
plt.xlabel("Escala logarítmica")
plt.ylabel("Escala logarítmica")
plt.grid()

x=np.linspace(0,6,30)
plt.figure()
plt.scatter(x, np.cos(x))

theta=np.linspace(0,8*np.pi,100)
radio=2*theta
plt.figure()
plt.polar(theta,radio,'b.-')
plt.grid(visible=True)
plt.title("Espiral en polares")'''

'''Otros dibujos: step, '''


# Abrir el archivo CSV en modo lectura
with open('coches.dat', 'r') as file:
    # Crear un lector CSV
    lineas=file.readlines() 
    f=len(lineas)
    n=np.zeros([f])
    i=0
    # Leer cada fila del archivo CSV
    for row in lineas:
        n[i]=float(row)
        i+=1

minimo=np.min(n)
maximo=np.max(n)

plt.figure()

plt.subplot(1,3,1)
plt.hist(n)
plt.grid(visible=True)
plt.title("10 intervalos")
plt.xlabel("Coches por cada 1000 habitantes")
plt.ylabel("Número de paises")
plt.subplot(1,3,2)
plt.hist(n, bins=5)
plt.grid(visible=True)
plt.title("5 intervalos")
plt.xlabel("Coches por cada 1000 habitantes")
plt.ylabel("Número de paises")
plt.subplot(1,3,3)
plt.hist(n,bins=20)
plt.grid(visible=True)
plt.title("20 intervalos")
plt.xlabel("Coches por cada 1000 habitantes")
plt.ylabel("Número de paises")


FFMpegWriter=manimation.writers["ffmpeg"]
metadata = dict(title="Movie Test", artist ="Me", comment="A red circle following a blue sine wave")
writer = FFMpegWriter(fps=15, metadata=metadata)

fig =plt.figure()
n=1000
x=np.linspace(0, 6*np.pi,n)
y=np.sin(x)
sine_line, =plt.plot(x,y,"b")
red_circle,=plt.plot([],[],"ro",markersize=10)
plt.xlabel("x")
plt.ylabel("sin(x)")

with writer.saving(fig,"movie_test.mp4",100):
    for i in range(n):
        x0=x[i]
        y0=y[i]
        red_circle.set_data([x0],[y0])
        writer.grab_frame()



gifWriter=manimation.writers['pillow']
metadata = dict(title="Movie Test", artist ="Me", comment="A red circle following a blue sine wave")
writer = gifWriter(fps=15, metadata=metadata)

fig =plt.figure()
n=1000
x=np.linspace(0, 6*np.pi,n)
y=np.sin(x)
sine_line, =plt.plot(x,y,"b")
red_circle,=plt.plot([],[],"ro",markersize=10)
plt.xlabel("x")
plt.ylabel("sin(x)")

with writer.saving(fig,"movie_test.gif",100):
    for i in range(n):
        x0=x[i]
        y0=y[i]
        red_circle.set_data([x0],[y0])
        writer.grab_frame()






