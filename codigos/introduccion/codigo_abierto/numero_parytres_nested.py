#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 15:31:19 2024
Script para crear una función que comprueba si un número es par
si no lo es comprueba si es divisible por 3.
Script to create a function tha checks if a number is even else,
if can be divided by 3
@author: juan
"""

def parthreenested(n):
    ''' 
    Esta función toma como entrada un número n. Si n es par devuelve un mensaje
    indicando que el número es par.
    Si no, compr
    This funtion takes an integer number n as imput. If n is even then
    it shows a message indicating the number is even.
    '''
    if n%2 == 0:
        print(str(n),' es un numero par')
        print(str(n),'is an even number')
        if n%3 == 0:
            print(str(n),' es un par numero divisible entre 3')
            print(str(n),'is an even & divisible by 3 number')
    elif n%3 == 0:
        print(str(n),' es un numero divisible entre 3')
        print(str(n),'is an number divisible by 3')
    else:
        print(str(n),' es un numero no es divisible entre 2 ni entre 3')
        print(str(n),'is not divisible by 2 neither by 3 ')
            
    return()

