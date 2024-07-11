#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 17:54:42 2024

@author: lia
Sistemas de ecuaciones
"""
import numpy as np

def diag_sys(A,b):
    [f,c]=np.shape(A)
    x=np.zeros(f)
    for i in range(f):
        x[i]=b[i]/A[i,i]
    return x

A=np.diag([1,2,3,4])
print(A)
b=np.ones([4,1])
print(b)    
x=diag_sys(A, b)
print(x)