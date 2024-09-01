# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 17:25:30 2024
Esto es un ejemplo para ver el comando import
This is an example on the use of the import command
@author: abierto
"""
#importamos el script entero esto no siempre es una buena idea
#we import the whole script although not always it is a good idea
import eq_seg_grado
e = 2
f = -4
g = 1
solplus, solminus = eq_seg_grado.soleq2(e, f, g)

print('Example_import:', solplus)
print('Example_import:', solminus)

print('eq_seg_grado:', eq_seg_grado.solplus)
print('eqseg_grado:', eq_seg_grado.solminus)