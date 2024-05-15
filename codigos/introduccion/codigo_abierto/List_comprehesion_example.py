#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 08:59:21 2024
Un par de funciones usando list comprehesion
A pair of function using list comprehesion
@author: juan
"""


def lc_demo(A):
    """
    ESta función busca los numeros pares en una lista A y los guarda en 
    una nueva lista B
    This function finds the odd number in list A, a created a new list
    B with them
    """
    B = [i for i in A if i%2 != 0]
    return B

def pair_cmh(A,B):
    """
    A and B are two list of numbers of the same lenght. The function build a list
    of pairs, taken one element from and one element from b with the condition that 
    they should be different. It doesn't the mater the order i.e (1,2) and (2,1)
    are different a valid'. But, but we will use a list comprehension

    """
    pares = [(i,j) for i in A for j in B if i != j]
    return(pares)