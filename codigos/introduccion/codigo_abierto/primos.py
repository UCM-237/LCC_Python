#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:22:29 2024
funcióne para obtener los primeros n numeros primos
En la primera empleamos un flag.
En la segunda empleamos la estructura for else
funtion to get the first n prime numbers
@author: juan
"""

def numpr(n):
    primos = [2] #introducimos 2 como el primer primo
                 #we take 2 as the first prime number
    i  = 0
    impar = 3 #tomamos 3 como el rpier impar para probar
              #we take 3 as the first odd number to test
    while i<n:
        pr = 1 #flag activation
        for i in primos:
            if impar%i == 0:
                pr = 0 #flag deactivation
                break
        if pr ==1:
            primos.append(impar)
        
        impar = impar + 2
    return(primos)
        
def numprels(n):
    primos = [2] #introducimos 2 como el primer primo
                 #we take 2 as the first prime number
    i  = 0
    impar = 3 #tomamos 3 como el primer impar para probar
              #we take 3 as the first odd number to test
    while i<n:
        for i in primos:
            if impar%i == 0:
                break
        else:
            primos.append(impar)
        
        impar = impar + 2
    return(primos)
        


        