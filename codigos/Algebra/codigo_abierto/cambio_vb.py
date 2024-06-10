#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 15:40:36 2024
Vector basis change
aB1 : vector a coordinates represented in base b1
B1 Basis in which ab1 is represented. Matrix each column represents a vector of
the basis
B2 Basis in which we want to represent vector aB1
aB2: vector a coordinates in base B2
If base B2 is omited the program takes B2 as canonical
@author: juan
"""
import numpy as np
import matplotlib.pyplot as plt

eps = np.finfo(np.float64).eps

def pintavec(v,ax,col='b'):
    '''just to draw a 3D vector'''
    
   
    ax.quiver(0, 0, 0, v[0], v[1], v[2],color=col,length=0.1, normalize=True)
    plt.axis('equal')
def basisch(aB1,B1,B2=np.array(0)):
    '''Cambio de base de B1 a B2
        Basis chage form B1 to B2
    '''
    if B2.shape == ():
        B2 = np.eye(B1.shape[0])
    if np.linalg.det(B1) < eps or np.linalg.det(B2) < eps:
        print('los vectores de al menos una de las bases no sol linealmente independientes')
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
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
    return(aB2)


