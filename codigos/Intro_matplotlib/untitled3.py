#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 12:33:27 2024

@author: lia
"""

import numpy as np

v=np.array([1,2,3,4])
print(v)
M=np.array([[1,2,3],[2,4,5],[5,4,3]])
print(M)

z=np.zeros((3,3))
print(z)
o=np.ones((3,5))
print(o)

print(v[2])
print(M[0,1])


a=np.array([1,2,3,4,5])
b=np.array([2,2,2,2])
if len(a)!=len(b):
    print("Los arrays tienen distinta longitud")
else:
    s=a+b

l1=[1,2,3,4]
l2=[2,2,2,2]
ls=l1+l2
lsuma=[]

for i in range(len(l1)):
    lsuma.append(l1[i]+l2[i])
    
    np.radians