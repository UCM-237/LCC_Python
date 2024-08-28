# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:08:39 2024

@author: abierto
"""

from random import random
dato = random()
if dato == 0.5:
    dato = 0
elif dato < 0.5:
    dato = -dato*10
else:
    dato = dato*10
print(dato)


####version 2 ######

dato = random()
if dato <= 0.3:
    chivato  = -1
elif dato > 0.3 and dato < 0.5 :
    chivato = -0.5
elif dato >= 0.5 and dato <= 0.7:
    chivato = 0
else:
    chivato = 1
print('dato=',dato)
print('chivato=',chivato)

####version funcion pa usar donde se quiera####

def martita(dato):
    if dato <= 0.3:
        chivato  = -1
    elif dato > 0.3 and dato < 0.5 :
        chivato = -0.5
    elif dato >= 0.5 and dato <= 0.7:
        chivato = 0
    else:
        chivato = 1
    return(dato,chivato)
    
