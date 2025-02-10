#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 16:19:12 2024

@author: lia
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as manimation

gifWriter=manimation.writers['pillow']
metadata = dict(title="Movie Test", artist ="Me", comment="A red circle following a blue sine wave")
writer = gifWriter(fps=15, metadata=metadata)

fig =plt.figure()
n=1000
x=np.linspace(0, 6*np.pi,n)
y=np.sin(x)
sine_line, =plt.plot(x,y,"b")
red_circle,=plt.plot([],[],"ro",markersize=10)
plt.xlabel("x")
plt.ylabel("sin(x)")

with writer.saving(fig,"movie_test.gif",100):
    for i in range(n):
        x0=x[i]
        y0=y[i]
        red_circle.set_data([x0],[y0])
        writer.grab_frame()






