# -*- coding: utf-8 -*-
"""
Euler's method for solving initial value problems
"""
import numpy as np


def euler(fun, xa, a, b, h):
    """
    Solves numerically the initial value problem dx/dt = fun(t, x),
    x(a) = xa, in the interval [a, b], using Euler's method.

    Parameters
    ----------
    fun : function
        right-hand side of the differential equation, fun(t, x). It must
        accept t and x as inputs, even if it does not depend explicitly
        on t, and return a value (or an array) with the shape of x.
    xa : number, list or numpy array
        initial condition x(a). For a system of equations, one value per
        equation.
    a, b : float
        initial and final values of t (a < b).
    h : float
        integration step. If (b-a)/h is not an integer, the step is
        slightly reduced so that the last time is exactly b.

    Returns
    -------
    t : numpy array
        times a, a+h, a+2h, ..., b
    x : numpy array
        solution: x[j, i] is the unknown number j at time t[i]
    """
    if a >= b:
        raise ValueError('I need an increasing interval')
    xa = np.atleast_1d(np.asarray(xa, dtype=float))
    # number of steps: (b-a)/h rounded up. The small number avoids an
    # extra step when, due to rounding errors, (b-a)/h gives something
    # like 11.000000000000002
    n = int(np.ceil((b - a)/h - 1e-9))
    h = (b - a)/n
    t = np.linspace(a, b, n + 1)
    x = np.zeros([xa.shape[0], n + 1])
    x[:, 0] = xa
    for i in range(n):
        x[:, i+1] = x[:, i] + h*fun(t[i], x[:, i])
    return t, x
