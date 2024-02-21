#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 17:42:09 2024

@author: lia
"""

import numpy as np
import matplotlib.pyplot as plt
import raices as rc

x=np.linspace(-2.5,2.5,100)
y=rc.f_prueba(x)
x_int=np.array([-2,2])
y_int=rc.f_prueba(x_int)
x1=np.array([-2,-2,2,2])
y1=np.array([0,y_int[0],0,y_int[1]])
plt.plot(x,y)
plt.plot(x1[0:2],y1[0:2],'r-')
plt.plot(x_int[0],y_int[0],'ro')
plt.plot(x1[2:4],y1[2:4],'b-')
plt.plot(x_int[1],y_int[1],'bo')
raiz,error,nit=rc.biseccion(rc.f_prueba,-2,2.5,0.001,50)
print("Biseccion")
print("Raiz \t Error \t Iteraciones")
print(raiz,error,nit)
plt.plot(raiz,rc.f_prueba(raiz),'go')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
raiz,error,nit=rc.regula_falsi(rc.f_prueba,-2,2.5,0.001,50)
print("Interpolacion")
print("Raiz \t Error \t Iteraciones")
print(raiz,error,nit)
raiz,error,nit=rc.newton_raphson(rc.f_prueba,rc.df_prueba,2.5,0.001,50)
print("Newton")
print("Raiz \t Error \t Iteraciones")
print(raiz,error,nit)
raiz,error,nit=rc.secant(rc.f_prueba,-1,0   ,0.001,50)
print("Secante")
print("Raiz \t Error \t Iteraciones")
print(raiz,error,nit)
