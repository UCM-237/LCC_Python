#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 14:50:48 2024
Este modulo implementa la funcion dumbdet que calcula el determinante de 
una matriz empleando la formula de Laplace. La función es recursiva, 
(se llama a si misma sucesivamente para calcular los cofactores necesarios). 
Desarrolla siempre por los elementos de la primera columna. 
(Es un prodigio de ineficiencia numerica, pero permite manejar bucles 
y funciones recursivas, asi que supongo que puede ser útil para los que 
empiezan a programar).
un posible ejercicio para ver lo malo que es el método, consiste ir
aumentando la dimension de la matriz y comparar lo que lo tarde en
calcular el determinante con lo que tarda la función de numpy.linalg.det...
this module implements the function poordet which calculates a matrix 
determinant using the Laplace's formulae. It is a recursive function, 
(it calls itself on and on to calculate the cofactor nedded to get the 
 determinat). It always develod the formula using the elements of the matrix
first column.
(It is the most ineficient functionever writen, but may be an example of loops 
 and recursive functions  for begginers)
@author: juan
"""
import numpy as np
def dunmbdet(A):

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
            d = (-1)**(i+2)*A[i,0]*dunmbdet(N[:,1:sz])+d
            
    
    return d