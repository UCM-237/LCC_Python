#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:50:05 2024

@author: lia
"""

import numpy as np
import json as js

# Create a random 20x4 matrix
m2=np.random.random([20,4])

#Save it as a csv file
np.savetxt('randomMat.csv',m2, fmt='%.2f', delimiter=',')

#Read ir back with loadtxt
m3=np.loadtxt('randomMat.csv',delimiter=',')

print(m3)

robot=    {
  "id": "Frodo",
  "tipo" : "Hobbit",    
  "estado":{
      "posicion": [2.345,-5.985],
      "velocidad lineal": 0.15,
      "velocidad angular": 0,
      "baterias": 7.32
      }
}


js.dump(robot,open('jsondat.json','w'))

mi_robot=js.load(open('jsondat.json','r'))

print(mi_robot)
'''

arr=np.array([[0.3,4.3,3.5],[-1.23,0.032,-3.23]])
np.savetxt('matrix01.txt', arr,fmt='%.3f',delimiter=' ',header='Col1 Col2 Col3')

f=open('matrix01.txt','r')
print(f.read())
f.close()

#Now we read it with loadtxt

m1= np.loadtxt('matrix01.txt')
print(m1)


f=open('textfile.txt','w')
for i in range(5):
    f.write(f"Line {i}\n")
f.close()

f=open('textfile.txt','r')
print(f.read())
f.close()

f=open('textfile.txt','a')
f.write("Another line")
f.close()

f=open('textfile.txt','r')
print(f.readlines())
f.close()

f=open('textfile.txt','r')
while True:
    line=f.readline()
    if not line:
        break
    print(line)

f.close()
'''