# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 17:22:30 2024

@author: abierto
"""

def soleq2(a,b,c):
    """
    Esta función calcula las soluciones de la ecuación general,
    ax**2 + b*x + c = 0
    Variables de entrada:
        coeficientes a, b y c
    Variables de salida:
        xp Solucion para la raíz cuadrada positiva
        xm solucion para la raiz cuadrada negativa
        
    this function calculates the solutions of the general equation
    a*x**2 + b*x + c = 0
    input variables:
        a,b and c coeficients
    output variables;
        xp solution using positive square root
        xm solutions using negative square root
    """
    xp = (-b+(b**2-4*a*c)**(1/2))/2/a
    xm = (-b-(b**2-4*a*c)**(1/2))/2/a
    return xp, xm

#aquí añadimos un ejemplo de uso que no es parte de la funcion
#here we add a 'how to use' example that's not part of the function

solplus, solminus = soleq2(2, 3, 1)

#comprobacion
#checking
print('raíz positiva/positive root:', 2*solplus**2+3*solplus+1)
print('raiz negativa/negative root:', 2*solminus**2+3*solminus+1)