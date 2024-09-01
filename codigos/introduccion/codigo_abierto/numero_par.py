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
