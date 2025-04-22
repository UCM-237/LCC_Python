#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 14:51:17 2025
Normal distribution. Examples
Ejemplos distribución normal
@author: juan
"""
import numpy as np
from scipy.stats import norm

#we firs call the functions of norm directly
x = np.linspace(-5, 5,7)
p = np.linspace(0,1,7)
print('x=',x,'\n')
print('p=',p,'\n')
#normal distribution standard
y = norm.pdf(x)
print('pdf standard',y,'\n')

#normal cumulative distribution
ycum = norm.cdf(x)
print('cdf standard',ycum,'\n')

#normal inverse cumulative distribution
val = norm.ppf(p)
print('ppf standard',val,'\n')

#now, we introduce a mean value and a std deviation
mean =10 #mean
std = 5 #std dev

#normal distribution mean = 10 std dev = 5
y = norm.pdf(x,mean,std)
print('pdf m=10,std=5',y,'\n')

#normal cumulative distribution
ycum = norm.cdf(x,mean,std)
print('cdf m=10,std=5',ycum,'\n')

#normal inverse cumulative distribution
val = norm.ppf(p,mean, std)
print('ppf m=10,std=5',val,'\n')

#alternatively we can define a normal distribution with a predefined mean and
#standar deviation
norm_10_5 = norm(loc=10,scale=5)
print('mean and std predefined \n')
#normal distribution mean = 10 std dev = 5
y = norm.pdf(x,mean,std)
print('pdf m=10,std=5',y,'\n')

#normal cumulative distribution
ycum = norm.cdf(x,mean,std)
print('cdf m=10,std=5',ycum,'\n')

#normal inverse cumulative distribution
val = norm.ppf(p,mean, std)
print('ppf m=10,std=5',val,'\n')
