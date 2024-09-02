# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 11:18:38 2024

@author: abierto
"""

import numpy as np
import matplotlib.pyplot as pl

# for h in np.arange(1e-10,1e-8,1e-9):
#     y = np.sin(h)**2
#     dy = y/h
#     pl.plot(h,abs(dy),'o')
h = np.arange(3e-1,1.4,5e-2)
y = 3*h**3-2*h
dy = y/h

i = np.where(abs(dy) == min(abs(dy)))
fig, ax = pl.subplots() 
ax.plot(h[:-1],abs(dy[:-1]),'ok')
ax.plot(h[i],abs(dy[i]),'or')
ax.plot(h[i]*np.ones([2]),[0,max(abs(dy))],'--')
ax.annotate('valor óptimo \n optimal value',xy=(h[i],abs(dy[i])),\
            xytext=(0.5,0),\
arrowprops=dict(facecolor='black', shrink=0.05,width=0.5,headwidth=4))
ax.text(0.27,3.2,\
'Dominan errores de redondeo \n Rounding-off error dominate')
ax.text(0.82,3.2,\
'Dominan errores de truncamiento \n Truncating error dominate')
pl.xlabel('h')
pl.ylabel('error')
