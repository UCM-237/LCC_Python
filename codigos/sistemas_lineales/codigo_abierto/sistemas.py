#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 17:54:42 2024

@author: lia
Sistemas de ecuaciones
"""
import numpy as np
import scipy as sc 

def diag_sys(A,b):
    [f,c]=np.shape(A)
    x=np.zeros([f,1])
    for i in range(f):
        x[i]=b[i]/A[i,i]
    return x

def progressive(A,b):
    ''' This function computes the solution of a lower equation system using 
    progressive substitution. It receives the coefficient matriz A and the 
    independent term vector b. It returns the vector solution x
    '''
    # Coefficient matrix size. Return error if not square
    [f,c]=np.shape(A)
    if f!=c:
        print("A is not square")
        return
    # To build the solution vector x
    x=np.zeros(f)
    x=b
    for i in range(f):
        '''The inner block subtracts to the independent term the previous solution
         multiplied by the correspondent coefficient'''
        for j in range(0,i):
            x[i]-=x[j]*A[i,j]
        '''Finaly divide the result by the diagonal coefficient'''
        x[i]=(x[i])/A[i,i]
    return x

def regressive(A,b):
    ''' This function computes the solution of a upper equation system using 
    regressive substitution. It receives the coefficient matriz A and the 
    independent term vector b. It returns the vector solution x
    '''
    # Coefficient matrix size. Return error if not square
    [f,c]=np.shape(A)
    if f!=c:
        print("A is not square")
        return
    # To build the solution vector x
    x=np.zeros(f)
    x=b

    for i in range(f-1,-1,-1):
        '''The inner block subtracts to the independent term the previous solution
         multiplied by the correspondent coefficient'''
        for j in range(i+1,f,1):
            x[i]-=x[j]*A[i,j]
            
        '''Finaly divide the result by the diagonal coefficient'''
        x[i]=(x[i])/A[i,i]
    return x

def eligauss(A):
    '''This function obtains an upper triangular matrix, starting from a given
    matrix, by applying the Gaussian elimination method.
    It does not perform row piboting'''
    
    #Matrix shape
    [f,c]=np.shape(A)
    U=A
    #For all the columns in A (except the last one)
    for i in range(c-1):
        # For all the rows below the diagonal
        for j in range(i+1,f):
            U[j,:]=U[j,:]-U[i,:]*U[j,i]/U[i,i]
    return U


def eligaussp(A):
    '''This function obtains an upper triangular matrix, starting from a given
    matrix, by applying the Gaussian elimination method.
    It includes row piboting. If the diagonal element is less than the same
    element in next rows, rows are interchanged'''
   
    #Matrix shape
    [f,c]=np.shape(A)
    U=A
    #For all the columns in A (except the last one)
    for i in range(c-1):
        #Row pivoting
        # Search the maximun in column i
        maxcol= np.abs(U[i,i])
        index = i
        for l in range(i,f):
            if np.abs(U[l,i])>maxcol:
                maxcol=np.abs(U[l,i])
                index=l
        # If we have found an element U[l,i] greater than U[i,i] we interchange
        # row l with row i
        if index!=i:
            aux=np.array([U[i,:]])
            U[i,:]=U[index,:]
            U[index,:]=aux[:]
        # End of Row pivoting
        # For all the rows below the diagonal
        print(U)
        for j in range(i+1,f):
            U[j,:]=U[j,:]-U[i,:]*U[j,i]/U[i,i]
    return U


def gaussjordan(A):
    '''This function implements gauss-jordan elimination to obtain a diagonal
    matrix'''    
    
    #Matrix shape
    [f,c]=np.shape(A)
    U=A
    # Step 1: reduce matrix A to a triangular matrix
    #For all the columns in A (except the last one)
    for i in range(c-1):
        #Row pivoting
        # Search the maximun in column i
        maxcol= np.abs(U[i,i])
        index = i
        for l in range(i,f):
            if np.abs(U[l,i])>maxcol:
                maxcol=np.abs(U[l,i])
                index=l
        # If we have found an element U[l,i] greater than U[i,i] we interchange
        # row l with row i
        if index!=i:
            aux=np.array([U[i,:]])
            U[i,:]=U[index,:]
            U[index,:]=aux[:]
        # End of Row pivoting
        # For all the rows below the diagonal
        print(U)
        for j in range(i+1,f):
            U[j,:]=U[j,:]-U[i,:]*U[j,i]/U[i,i]
    # Step 2: obtain the diagonal matrix
    # For all the columns begining by the end
    for i in range(c-2,-1,-1):
        # For all the rows above the diagonal
        for j in range(i-1,-1,-1):
            U[j,:]=U[j,:]-U[i,:]*U[j,i]/U[i,i]
    return U

'''A=np.diag([1,2,3,4])
print(A)
b=np.ones([4,1])
print(b)    
x=diag_sys(A, b)
print(x)


A=np.array([[2,0,0,0],[3,2,0,0],[2,5,7,0],[1,-2,3,4]])
b=np.ones([4,1])
x=progressive(A, b)
print(x)
print(np.dot(A,x))

A=np.array([[1, 3, 2],[2, -1, 1],[1, 4, 3]])
b=np.array([[13],[3],[18]])
cond=np.linalg.cond(A)
P,L,U=sc.linalg.lu(A)
print("L:",L)
print("U:",U)
print("P: ",P)
Pb=np.transpose(P).dot(b)
print("Pb: ",Pb)
z=progressive(L, Pb)
print("z:",z)
print("Lz: ",L.dot(z))
x=regressive(U, z)
print("x:",x)
print(A.dot(x))


A=np.array([[2., 5., 1.],[5., 14., 2.],[1., 2., 6.]])
b=np.array([[15.],[39.],[23.]])
L=sc.linalg.cholesky(A,lower=True)
print("L: ",L)
z=progressive(L, b)
print("z: ",z)
LT=np.transpose(L)
print("LT: ",LT)
x=regressive(LT,z)
print("x: ", x)
print(A.dot(x))

# QR factorising
A=np.array([[1, 3, 2],[2, -1, 1],[1, 4, 3]])
b=np.array([[13],[3],[18]])
Q,R=sc.linalg.qr(A)
print("Q: ",Q)
print("R: ", R)
Qb=np.transpose(Q).dot(b)
x=regressive(R, Qb)
print("x: ",x)
#SVD decomposition
A=np.array([[1, 3, 2],[2, -1, 1],[1, 4, 3]])
b=np.array([[13],[3],[18]])
U,s,V=sc.linalg.svd(A)
print("U: ",U)
print("V: ",V)
print("s: ",s)
S=np.diag(s)
print("S: ",S)
Utb=np.transpose(U).dot(b)
z=diag_sys(S, Utb)
print("z: ",z)
x=np.transpose(V).dot(z)
print("x:",x)

A=np.array([[3.,4.,2.,5.],[2.,0.,1.,-2.],[3.,2.,1.,8.],[5.,2.,3.,2.]])
print(A)
U=eligauss(A)
print(U)

A=np.array([[1., 3., 2.],[2., -1., 1.],[1., 4., 3.]])
b=np.array([[13.],[3.],[18.]])
# Extended matrix
AM=np.concatenate((A,b),axis=1)
print("AM: ",AM)
GA=eligaussp(AM)
print("GA: ",GA)
RA=GA[:,0:3]
nb=GA[:,3]
print("RA: ",RA)
print("nb: ",nb)
x=regressive(RA, nb)
print("x: ",x)'''

A=np.array([[1., 3., 2.],[2., -1., 1.],[1., 4., 3.]])
b=np.array([[13.],[3.],[18.]])
# Extended matrix
AM=np.concatenate((A,b),axis=1)
print("AM: ",AM)
U=gaussjordan(AM)
print(U)
RA=U[:,0:3]
x=U[:,3]
x=x/np.diag(RA)
print(x)