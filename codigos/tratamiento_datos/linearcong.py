#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador lineal congruencial / linear congruential generator
@author: juan
"""
import matplotlib.pyplot as pl


def linear_con(i0, a, c, m, l):
    """
    i0: semilla / seed, 0 <= i0 < m
    a: multiplicador / multiplier, 0 <= a < m
    c: incremento / increment, 0 <= c < m
    m: módulo / modulus (cuanto mayor, mejor / the larger the better)
    l: número de elementos de la secuencia / length of the sequence

    Devuelve una lista de l números en [0, 1) / returns a list of l numbers
    in [0, 1)
    """
    secuencia = []
    for i in range(l):
        i0 = (a*i0 + c) % m
        secuencia.append(i0/m)
    return secuencia


# Ejemplo con parámetros muy usados (Numerical Recipes): m = 2**32
# Example with widely used parameters (Numerical Recipes): m = 2**32
sec = linear_con(1000, 1664525, 1013904223, 2**32, 1000)
print(len(sec), min(sec), max(sec))
pl.plot(sec, '.')
