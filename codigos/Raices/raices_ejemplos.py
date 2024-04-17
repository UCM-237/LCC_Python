#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 17:42:09 2024

@author: lia
"""

import numpy as np
import matplotlib.pyplot as plt
import raices as rc
import scipy.optimize as opt
from numpy.polynomial import Polynomial as P


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

def fun(x):
    y=np.exp(x)-x**2
    return y

roots=opt.fsolve(fun,-2)
print("fsolve roots")
print(roots)

p = P([0,6,2,0,3])
print(p)

#y(x)=x^3-6^2+11x-6
p1=P([1,-6,11,-6])
print(p1)
print("The roots are:\t",p1.roots())

p2=P([1,2,1])
print(p2)
print("The roots are:\t",p2.roots())

#Create a polynomial with roots 3, -2, 2
p3=P.fromroots([3,-2,2])
print(p3)
#Compute the polynomial that is its derivative
pdot=p3.deriv()
print("Derivative:", pdot)
#Compute the polynomial that is the integral
pint=p3.integ()
print("Integral:", pint)
#Create polynomial p4 as a copy of pint
p4=pint.copy()
print(p4)
'''
print(p1*p2)
print(p//p2)
print(p%p2)
print(p**2)

#Polynomial p created and domain defined as [-2,2]
p=P([0,6,2,0,3],[-2,2])
dat=p.linspace()
plt.figure()
plt.grid()
plt.plot(dat[0],dat[1])
plt.xlabel('x')
plt.ylabel('y')
p_string=str(p)
plt.title(p_string)'''