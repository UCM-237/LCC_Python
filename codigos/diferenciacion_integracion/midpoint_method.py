# -*- coding: utf-8 -*-
"""
The Runge-Kutta midpoint method for solving initial value problems
"""
import numpy as np


def pmedio(fun, xa, a, b, h):
    """
    Solves numerically the initial value problem dx/dt = fun(t, x),
    x(a) = xa, in the interval [a, b], using the midpoint method
    (second-order Runge-Kutta).

    Parameters
    ----------
    fun : function
        right-hand side of the differential equation, fun(t, x).
    xa : number, list or numpy array
        initial condition x(a).
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
    n = int(np.ceil((b - a)/h - 1e-9))
    h = (b - a)/n
    t = np.linspace(a, b, n + 1)
    x = np.zeros([xa.shape[0], n + 1])
    x[:, 0] = xa
    for i in range(n):
        # half a step with Euler, to estimate x at the midpoint
        xm = x[:, i] + h/2*fun(t[i], x[:, i])
        # whole step with the slope at the midpoint
        x[:, i+1] = x[:, i] + h*fun(t[i] + h/2, xm)
    return t, x
