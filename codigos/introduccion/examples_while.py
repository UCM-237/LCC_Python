#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:46:35 2024
Un par de ejemplos de uso de bucles while
A pair of loop while examples
@author: juan
"""

def pmax(a,M):
    """ 
    This funtion optain the minimum exponent n such that a**n >= M
    esta funci-on optiene el minimo esponte n tal que a**n >= M
    """
    n = 0
    while a**n < M:
        n = n+1
    return n

def L_suma(A,B):
    """
    This function take tho list of list of numbers A and B and adds the numbers 
    located at the same position in both list. (both lists should have the
    same dimensions)
    Esta función toma dos listas A y B y crea una nueva lista con la suma de los
    números que ocupan la misma posición (ambas listas deben tener las mismas
    dimensiones)
    """
    
    i = 0 #indice de para recorrer las listas de números
          #numbers to cover the list of number list
    C =[]
    n_lista = len(A)
    while i < n_lista:
        n_num = len(A[i])
        j = 0 #indice para recorrer los numeros de cada lista de numeros 
              #index to cover the number of each number list
        C.append([])
        while j < n_num:
            C[i].append(A[i][j]+B[i][j])
            j = j+1
        i = i+1
    return C