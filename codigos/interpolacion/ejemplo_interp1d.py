# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 16:55:04 2024
Piecewise interpolation with NumPy and SciPy (revised 2026)
@author: abierto
"""
import numpy as np
from scipy.interpolate import interp1d, CubicSpline
from matplotlib import pyplot as pl

x = np.array([ 1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.])
y = np.array([-1.8143451, 20.914356, 26.714303, 61.129501,
              76.414728, 123.00032, 167.06809, 212.97832,
              258.67911, 320.53422])
pl.plot(x, y, 'o', label='data')
# points at which we want to interpolate
xi = np.linspace(1, 10, 500)

# linear interpolation: np.interp(points, x data, y data)
yi = np.interp(xi, x, y)
pl.plot(xi, yi, label='linear')

# zero-order interpolation: interp1d (a 'legacy' SciPy function)
# returns a function that we then evaluate at xi
fnear = interp1d(x, y, kind='nearest')
pl.plot(xi, fnear(xi), label='nearest')
fprev = interp1d(x, y, kind='previous')
pl.plot(xi, fprev(xi), label='previous')

# cubic splines: CubicSpline also returns a function
spnat = CubicSpline(x, y, bc_type='natural')
pl.plot(xi, spnat(xi), label='natural spline')
pl.legend()
pl.show()
