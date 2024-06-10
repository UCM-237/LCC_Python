#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:45:01 2024

@author: lia
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

x=np.linspace(0,2,100)
y=np.sin(2*np.pi*x)
z=np.cos(2*np.pi*x)

fig,ax=plt.subplots(subplot_kw={"projection": "3d"})
ax.scatter(x,y,z)

# Make data
x=np.linspace(-1.5,1.5,25)
y=np.linspace(-2,2,50)
[Xm,Ym]=np.meshgrid(x,y)

Zm=Xm**3+Ym**2
# Plot the surface
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_wireframe(Xm, Ym, Zm)

ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

plt.show()


fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(Xm, Ym, Zm)

ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

plt.show()