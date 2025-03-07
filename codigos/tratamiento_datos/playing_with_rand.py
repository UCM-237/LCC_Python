#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 16:13:56 2025
Playing with random numbers
@author: juan
"""

import numpy as np

#lo primero de todo es crear un generador de números aleatorios
#si no le indicamos semilla, el la toma del sistema operativo de modo no
#determinista, es decir la secuencia de números generada no podrá volver a 
#reproducirse.

gen_num = np.random.default_rng()

#generamos un numero aleatorio entre [0,1)
n1 = gen_num.random()
print(n1)

#generamos un numero aleatorio entero entre dos límites dados [bajo,alto)
n2 = gen_num.integers(2,5)
print(n2)

