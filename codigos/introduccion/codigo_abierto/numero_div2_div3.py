#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 15:31:19 2024
Script para crear una función que comprueba si un número es par y si no lo es 
comprueba si es divisible por tres
Script to create a function tha checks if a number is even
@author: juan
"""


def parthree(n):
    ''' 
    Esta función toma como entrada un número n y muestra un mensaje
    indicando si el número es par si no comprueva si es divisible por 3
    This function takes an integer number n as input and checks if the
    number is even. If not it checks if the number is divisble by 3
    '''
    if n%2 == 0:
        print(str(n),' es un numero par')
        print(str(n),'is an even number')
    elif n%3 ==0:
        print(str(n),' es un numero divisible por tres')
        print(str(n),'is a number divisible by three')
    else:
        print(str(n),' es un numero impar pero no divisible por tres')
        print(str(n),'is an odd number but it not divisible by three')
    return()        