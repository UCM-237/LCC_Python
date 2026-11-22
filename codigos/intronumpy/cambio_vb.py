#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 15:40:36 2024
Vector basis change
aB1: coordinates of vector a in basis B1
B1: basis in which aB1 is represented. Each column of the matrix is a vector of
the basis
B2 Basis in which we want to represent vector aB1
aB2: coordinates of vector a in basis B2
If basis B2 is omitted, the program takes the canonical basis as B2
@author: juan
"""
import numpy as np
import matplotlib.pyplot as plt

eps = np.finfo(np.float64).eps

def pintavec(v,ax,col='b'):
    '''dibuja un vector 3D desde el origen / just to draw a 3D vector'''
    ax.quiver(0, 0, 0, v[0], v[1], v[2], color=col, arrow_length_ratio=0.1)
def basisch(aB1,B1,B2=np.array(0)):
    '''Cambio de base de B1 a B2
        Basis change from B1 to B2
    '''
    if B2.shape == ():
        B2 = np.eye(B1.shape[0])
    # una base debe tener rango completo (¡ojo!: det(B) puede ser negativo)
    # a basis must have full rank (beware: det(B) may be negative)
    n = B1.shape[0]
    if np.linalg.matrix_rank(B1) < n or np.linalg.matrix_rank(B2) < n:
        print('los vectores de al menos una de las bases no son linealmente independientes')
        print('the vectors of at least one of the bases are not linearly independent')
        return([])
    aB2 = np.linalg.inv(B2)@B1@aB1
    if B1.shape[0] == 3:
        #draw the vector
        ax = plt.figure().add_subplot(projection='3d')
        for i in B1.T:
            pintavec(i,ax)
        for i in B2.T:
            pintavec(i,ax,'r')
        pintavec(B1@aB1,ax,'k')
        pintavec(B2@aB2,ax,'g')
        # mismos límites en los tres ejes / same limits on the three axes
        m = np.abs(np.hstack((B1, B2, (B1@aB1)[:, None]))).max()
        ax.set_xlim(-m, m)
        ax.set_ylim(-m, m)
        ax.set_zlim(-m, m)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
    return(aB2)


