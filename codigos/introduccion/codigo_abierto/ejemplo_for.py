#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 15:08:34 2024
Este modulo contiene algunos ejemplos del uso de los bucles for
This module contains some examples of for loops use
@author: juan
"""

def sumalist(A):
    """
    Input A should be a list of numbers no mater how long
    the function shows the values on the screen, sum them and save the result
    in the returned variable y
    
    La entrada A debe ser una lista de números the cualquier longitud. 
    La funcion muestra los valore de la lista, los suma y devuelve el resultado
    en la variable y
    """
    y = 0 #definimos la variable en la que guardaremos el resultado de la suma
          #define the variable to save the result of the sum
    for i in A:
        print(i)
        y = y + i
    return y

def sumaelementos(A,B):
    """ 
    Inputs A and B shoudd be two list of numbers with the same length
    The funtion calculates the sum of the elements of A and B that share the
    same location inside their respective list i.e. The result is save
    in list S in the same location: S[i] = A[i]+B[i]
    """
    
    if len(A) != len(B):
        print('Las listas que me das no son igual de largas')
        print('Sling your hook! The lists lengths are different. ')
        return([]) #we return an empty list
    else:
        S = []
        index = range(len(A)) #index to cover the elements of A&B
        for j in index:
            S.append(A[j] + B[j]) #adding the elements in the same location
            
        return(S)
            
def firsttime(A,b):
    """
    esta función busca la primera ves que un número b aparece en una list
    A y devuelve su posición dentro de la lista. 
    Si no aparece muestra un mensaje por pantalla
    This program find the first time a number b apears in a list A
    """
    p =0
    for i in A:
        if i==b:
            return(p)
            break
        p = p + 1 #p += 1
    print('el numero no esta en la lista')
    print('the number is not in the list')
    return('no esta')

def buscapar(A):
    """
    Esta funcion busca los numeros pares de una lista de numeros y 
    crea una nueva lista solo con los pares contenidos en la lista inicial
    """
    B = [] #and empty list to save the even numbers
    for i in A:
        if i%2 !=0:
            continue
        B.append(i)
    return B


def listadelistas(A,b):
    """
    Esta funcion busca las veces que aparece un número en una lista
    bidimensional (una lista de listas de números)
    Devuleve las veces que aparece el número y los indices de las posisiciones
    en que aparece.
    """
    ind = [] #an empty list to save the list indexes  where the number is.
    counter = 0 #number of times the number is repeated in the list
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] == b:
                ind.append((i,j))
                counter = counter+1
                
    return(ind,counter)
 
def pairs(A,B):
    """
    A and B are two list of numbers of the same lenght. The function build a list
    of pairs, taken one element from and one element from b with the condition that 
    they should be different. It doesn't the mater the order i.e (1,2) and (2,1)
    are different a valid'

    """
    pares = [] #an empty list
    for i in A:
        for j in B:
            if i != j:
                pares.append((i,j))
    return(pares)
