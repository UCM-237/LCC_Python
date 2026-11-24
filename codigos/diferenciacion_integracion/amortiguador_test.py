# -*- coding: utf-8 -*-
"""
Damped oscillator (a mass hanging from a spring, with a damper)
solved with Euler's method
"""
import numpy as np
import matplotlib.pyplot as pl
from Euler_method import euler


def amortiguador(t, y, k=10., m=2., mu=0.5, g=9.8):
    """
    Right-hand side of the equations of the damped oscillator,
        dy/dt = v,  dv/dt = g - (k/m)*y - (mu/m)*v

    y[0] is the position (m) and y[1] the velocity (m/s); k is the
    spring constant (N/m), m the mass (kg), mu the damping constant
    (kg/s) and g the gravity acceleration (m/s^2).
    Returns the array [dy/dt, dv/dt].
    """
    return np.array([y[1], g - (k/m)*y[0] - (mu/m)*y[1]])


t, y = euler(amortiguador, [0, 0], 0, 50, 0.01)
pl.plot(t, y[0], label='y (m)')
pl.plot(t, y[1], label='v (m/s)')
pl.xlabel('t (s)')
pl.title('k = 10 N/m, h = 0.01 s')
pl.legend()
