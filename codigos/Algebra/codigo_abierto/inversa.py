# -*- coding: utf-8 -*-
"""
Created on Sat May 25 17:47:28 2024
Este módulo implementa la funcion inver, que calcula la inversa
de una matriz cuadrada empleando la expresión clásica
A^-1 = [adj(A)]^T*det(A)
EL determinante de la matriz se obtiene empleando la función
dumbdet incluida en el módulo determinante
@author: abierto
"""
import numpy as np
from determinante import dumbdet
def inver(A):
    """
    Esta función devuelve la inversa de una matriz cuadrada A
    """
    # primero comprobamos que la matriz suministrada 
    #es cuadrada:
    f = A.shape[0]
    #creamos una matriz de ceros del mismo tamaño
    iA = np.zeros((f,f))
    if f != A.shape[1]:
        print('la matriz no es cuadrada, Campeón')
        return();
    else:
        #calculamos el determinante de A, si es cero hemos terminado
        dA=dumbdet(A)
        if dA==0:
            print('la matriz es singular, la pobre')
            return()
        
        if abs(dA) <= 10*np.finfo(float).eps:
            print('cuidado determinante proximo a cero')
        
    
        #Calculamos el cofactor de cada
        #término de A mediante un doble bucle.
        for i in range(f):
            for j in range(f):
                # Construimos el menor correspondiente al elemento (i,j)
                m=np.delete(np.delete(A,i,0),j,1)
                
                #calculamos el cofactor llamando a la función determinante
                #lo ponemos ya en la posición que corresponderia a la matriz 
                # transpuesta de la adjunta.
                iA[j,i]=(-1)**(i+j)*dumbdet(m)
                
    
    #Terminamos la operacion dividiendo por el determinante de A
        iA=iA/dA
        return(iA)