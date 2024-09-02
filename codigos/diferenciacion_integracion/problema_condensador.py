# -*- coding: utf-8 -*-
"""
Script de python para resolver numericamente el problema del condensador
integrando la ecuación difercial mediante el método de Euler
"""

import numpy as np

import matplotlib.pyplot as pl #libreria de python para dibujar gráficas


def condensador(R, C, Vs,V0):
    ''' Esta función define la derivada del voltaje con respecto al tiempo en
    los terminales de un condensador de capacidad C, en un circuito RC serie
    El valor de la resistencia es R, la fuente de tensión ideal toma valor Vi
    
    
    variables de entrada:
        R resitencia en ohmios
        C capacidad en faradios
        V0 voltaje al que está el condensador
        Vs voltaje de la fuente de alimentación
    Variables de salida:
        dotV derivada de la tension en el condensador con respecto al tiempo
    ''' 
    dotV = (Vs-V0)/R/C
    return dotV
    
#integramos empleando el método de Euler para el caso en que la fuente 
#suministra un voltaje constante,

#definimos un tiempo final, hasta el que queremos calcular la solución
#tomamos el tiempo inicial como 0
tf = 1
#Vamos a usar varios pasos de integración para ver el efecto sobre la solucion
pt = [0.01, 0.05]

#definimos los valores de la resistencia, capacidad del condesador y voltaje de
#la fuente y el valor inicial de la tensión en el condesador

R = 1000
C = 0.0001
Vs = 10
V0 = 0
#empleamos un bucle para integrar la ecuación 'condesador' con los dos valores
#elegidos de dt
pl.figure(1)
for dt in pt:
    #aquí va el autentico bucle de cálculo empleando Euler
    V = [V0] #guardo el valor inicial del voltaje 
    t=0 #igualamos el tiempo a su valor inicial
    tiempos = np.arange(t,tf,dt) #creamos un vector de tiempo
    V = np.zeros(tiempos.shape) #y otro, para las tensiones del mismo tamaño
    V[0] = V0 #pongo V0 en el primer valor de V
    for i in range(tiempos.shape[0]-1):
        V[i+1] = V[i] + condensador(R,C,Vs,V[i])*dt
    pl.plot(tiempos,V)
    pl.plot(tiempos,V,'.') #pinto tambien cada punto obtenido por euler
    
#como en este caso la solución analítica es fácil la calculamos y las pintamos
#juntas
temp = np.arange(0,tf,0.0001) #uso un paso de tiempo mas fino
Va = Vs*(1-np.exp(-np.array(temp)/R/C))
pl.plot(temp,Va)
pl.xlabel('t s.')
pl.ylabel('V volt.')
pl.legend(['dt = 0.01','','dt = 0.05','','sol. analítica'])


#vamos ahora a darle una tensión sinusoidal para ver que pasa

def Voltios(Vm,w,t, ph=0):
    """
    input
    Voltaje sinusoidal
    Vm amplitud
    w frecuencia en rad/s
    t tiempo en s
    output
    V en voltios
    ph es la fase en rad, por defecto es cero
    """
    V = Vm*np.sin(w*t) 
    return V

#Repetimos todo igual que antes

R = 1000
C = 0.0001
Vm = 10
w = 10*np.pi #añadimos una frecuencia baja para que no nos mate el aliasing ja,ja
#así y todo se va a ver muy bien lo que pasa con el paso bajo de integración
#empleamos un bucle para integrar la ecuación 'condesador' con los dos valores
#elegidos de dt
pl.figure(2) #creo una nueva figura para no estropear la anterior
for dt in pt:
    #aquí va el autentico bucle de cálculo empleando Euler
      
    t=0 #igualamos el tiempo a su valor inicial
    tiempos = np.arange(t,tf,dt) #creamos un vector de tiempo
    V = np.zeros(tiempos.shape) #y otro, para las tensiones del mismo tamaño
    V[0] = Voltios(Vm,w,0) #guardo el valor inicial del voltaje
    for i in range(tiempos.shape[0]-1):
        V[i+1] = V[i] + condensador(R,C,Voltios(Vm,w,tiempos[i]),V[i])*dt
    pl.plot(tiempos,V)
    pl.plot(tiempos,V,'.') #pinto tambien cada punto obtenido por euler


Vs = Voltios(Vm,w,temp)
pl.plot(temp,Vs)    
pl.xlabel('t s.')
pl.ylabel('V volt.')
pl.legend(['dt = 0.01','','dt = 0.05','','vol. fuente'])