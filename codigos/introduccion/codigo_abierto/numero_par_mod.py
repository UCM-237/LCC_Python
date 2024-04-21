#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 15:31:19 2024
Script para crear una función que comprueba si un número es par
Script to create a function tha checks if a number is even
@author: juan
"""

def par(n):
    ''' 
    Esta función toma como entrada un número n. Si n es par devuelve un mensaje
    indicando que el número es par.
    This funtion takes an integer number n as imput. If n is even then
    it shows a message indicating the number is even.
    '''
    if n%2 == 0:
        print(str(n),' es un numero par')
        print(str(n),'is an even number')
    return()

def par2(n):
    ''' 
    Esta función toma como entrada un número n y muestra un mensaje
    indicando si el número es par o impar
    This function takes an integer number n as input and shows a message
    stating whether the number is even or odd
    '''
    if n%2 == 0:
        print(str(n),' es un numero par')
        print(str(n),'is an even number')
    else:
        print(str(n),' es un numero impar')
        print(str(n),'is an odd number')
    return()        