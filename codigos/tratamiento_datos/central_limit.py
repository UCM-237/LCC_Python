#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teorema central del límite con números aleatorios
Central limit theorem using random numbers
@author: juan
"""
import numpy as np
import matplotlib.pyplot as pl

# Semilla fija: la secuencia (y la figura) se puede reproducir
# Fixed seed: the sequence (and the figure) can be reproduced
gen_num = np.random.default_rng(1000)
N = 100_000            # número de experimentos / number of experiments


def normal(x, mu, s2):
    """Distribución normal de media mu y varianza s2"""
    return np.exp(-(x - mu)**2/(2*s2))/np.sqrt(2*np.pi*s2)


x = np.linspace(-0.9, 0.9, 400)
for k, n in enumerate([10, 100]):
    # N experimentos de n números uniformes en [-1, 1): una fila por
    # experimento; la media de cada fila es una muestra de la media
    # N experiments of n uniform numbers in [-1, 1): one row per experiment
    datos = 2*gen_num.random((N, n)) - 1
    medias = datos.mean(axis=1)
    s2 = (2**2/12)/n   # varianza que predice el teorema / predicted variance
    print(f'n={n:4d}: media {medias.mean():+.5f} (teoría 0), '
          f'varianza {medias.var():.6f} (teoría {s2:.6f})')
    ax = pl.subplot(1, 2, k + 1)
    # density=True normaliza el histograma: área total 1
    ax.hist(medias, bins=50, density=True)
    ax.plot(x, normal(x, 0, s2))
    ax.set_xlabel(r'$\bar{x}_{%d}$' % n)
    ax.set_ylabel('Densidad de probabilidad')
