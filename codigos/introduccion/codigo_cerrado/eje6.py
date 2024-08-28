# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:41:20 2024

@author: abierto
"""

n = 5
#a empty list of n empty lists of length n each,its python's magic!
#una lista de n listas vacia de tamaño n cada una, es la magia de python
x = []
for i in range(n):
    
for i in range(n):
    for j in range(n):
        if i == j:
            x[i][j] = 1
        elif abs(i-j) == 1:
            x[i][j] = -1
        else:
            x[i][j] = 0
            