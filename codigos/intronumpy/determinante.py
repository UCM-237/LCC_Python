#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 14:50:48 2024
Este módulo implementa la función dumbdet que calcula el determinante de 
una matriz empleando la formula de Laplace. La función es recursiva, 
(se llama a sí misma sucesivamente para calcular los cofactores necesarios). 
Desarrolla siempre por los elementos de la primera columna. 
(Es un prodigio de ineficiencia numérica, pero permite manejar bucles 
y funciones recursivas, así que supongo que puede ser útil para los que 
empiezan a programar).
Un posible ejercicio para ver lo malo que es el método consiste en ir
aumentando la dimensión de la matriz y comparar lo que tarda en
calcular el determinante con lo que tarda la función numpy.linalg.det...
This module implements the function dumbdet, which calculates the determinant
of a matrix using Laplace's formula. It is a recursive function
(it calls itself again and again to calculate the cofactors needed to get the
determinant). It always expands along the entries of the first column of the
matrix.
(It is a marvel of numerical inefficiency, but it is a good example of loops
and recursive functions for beginners.)
@author: juan
"""
import numpy as np
def dumbdet(A):

#first we check the matrix is square
#primero comprobamos si la matriz es cuadrada
    sz = A.shape[0]
    d = 0 #variable to save the result/ Variable para guardar el resultado
    
    if  sz != A.shape[1]:
        print('La matriz no es cuadrada')
        print('The matrix is not square')
        d = []
    elif sz == 1:
        return A[0,0]
    else:

        for i in range(0,sz):
            N = np.delete(A,i,0)
            d = (-1)**(i+2)*A[i,0]*dumbdet(N[:,1:sz])+d
            
    
    return d