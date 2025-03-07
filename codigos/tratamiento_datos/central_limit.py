#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 16:13:56 2025
EStudiamos el teorema central del límite, generando números aleatorios
@author: juan
"""

import numpy as np
#creamos un generador de números aleatorios,
#usamos una semilla para que se pueda reproducir tal cual
gen_num = np.random.default_rng(1000)

#generamos un ,millón de vectores, formados por número aletorios distribuidos
#en el intervalo [-1,1). calculamos el valor medio de los 10 elementos de
#cada vector y guardamos los resultados en un nuevo vector.
#esto puede llevar un rato
media10 = np.zeros(1000000) #vector para guardar las medias
for i in range(1000000):
    media10[i] = np.mean(2*gen_num.random([10,1])-1)
    
#repetimos el cálculo pero ahora con vectores de 100 elementos
media100 = np.zeros(1000000) #vector para guardar las medias
for i in range(1000000):
    media100[i] = np.mean(2*gen_num.random([100,1])-1)


