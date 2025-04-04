#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 17:04:52 2025
Playing with the electrical network data
@author: juan
"""

import pandas as pd
import matplotlib.pyplot as pl

generacion_mw = pd.read_csv('../../datos/generacion20250319MW.csv')
generacion_mw.rename(columns=generacion_mw.iloc[1], inplace = True)
generacion_mw.drop([0,1],inplace=True)
lista = generacion_mw.columns
for i in lista[1:]:
    generacion_mw[i] = generacion_mw[i].astype(float)
    
des = generacion_mw.describe()
des.loc['mean'][des.loc['mean']>0].plot.pie()

#cambio los índices a las horas que es bastante sensato
gn_Mw_h = generacion_mw.set_index('Hora')

#pido que me grafique todas, frente al tiempo queda un tanto faragoso
#pero da una idea de lo que hay
pl.figure()
gn_Mw_h.plot(rot=40,ylabel='Mw')
pl.figure()
gn_Mw_h.boxplot(rot=90)
#vamos a hacer un diagrama de quesos pero eliminado los negativos que propiamente
#no son produccion Seleccionamos una hora

datos1005 = gn_Mw_h.loc['2025-03-19 01:05','Eólica':]
datos1230 = gn_Mw_h.loc['2025-03-19 12:30','Eólica':]
datosprod1005 = datos1005[datos1005>0]
datosprod1230 = datos1230[datos1230>0]
pl.figure()
datosprod1005.plot.pie()
pl.figure()
datosprod1230.plot.pie()



