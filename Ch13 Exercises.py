#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 22:23:47 2018

@author: alexanderbayers
"""

import numpy as np
import matplotlib as mpl
import math
import scipy.stats as stats

#Exercise 1
if -1 > 0:
    x = -1
    y = 1
    
    if x >= 0 and y >= 0:
        z = 'both positive'
    elif x < 0 and y < 0:
        z = 'both negative'
    else:
        z = 'different signs'
    print(z)
    
#Exercise 2
N = 2000
innovations = np.random.randn(N)
y = np.zeros(N)


AR_params = np.array([1.4, -.8])
MA_params = np.array([.4, .8])

for i in np.arange(2, N):
    y[i] = AR_params[0]*y[i-1] + AR_params[1]*y[i-2] + MA_params[0]*innovations[i-1] + \
        + MA_params[1] * innovations[i-2]  + innovations[i]

filtered_series = y[1000:]
#mpl.pyplot.plot(filtered_series)

#Exercise 3
N = 2000
variance = np.ones(N)
y =np.zeros(N)
innovations = np.random.randn(N)

w  = 0.05
a = 0.05
b = .9

for i in np.arange(1, N):
    variance[i] = w + a * (y[i-1] ** 2) + b * variance[i-1]
    y[i] = innovations[i] * math.sqrt(variance[i])
    
filtered_variance = variance[1000:]
filtered_y = y[1000:]

#mpl.pyplot.plot(filtered_variance)
#mpl.pyplot.plot(filtered_y)

#Exercise 4
variance = np.full((2000), 10.0/9.0)
y =np.zeros(N)
innovations = np.random.randn(N)

w  = 0.05
a = 0.02
downvol = .07
b = .9

for i in np.arange(1, N):
    if (innovations[i-1] < 0): 
       downadjustment = downvol
    else:
        downadjustment = 0
    variance[i] = w + (a + downadjustment) * (variance[i-1]*(innovations[i-1]** 2)) + b * variance[i-1]
    y[i] = innovations[i] * math.sqrt(variance[i])
    
filtered_variance = variance[1000:]
filtered_y = y[1000:]

#Exercise 5
variance = np.full((2000), 10.0/9.0)
y =np.zeros(N)
innovations = np.random.randn(N)

w  = 0.05
a = 0.02
downvol = .07
b = .9
ar_param = -.1
ma_param = .4
lambda_param = .03

for i in np.arange(1, N):
    if (innovations[i-1] < 0): 
       downadjustment = downvol
    else:
        downadjustment = 0
    variance[i] = w + (a + downadjustment) * (variance[i-1])*(innovations[i-1] ** 2) + b * variance[i-1]
    y[i] = innovations[i] * math.sqrt(variance[i]) + ar_param*y[i-1] + \
        ma_param*math.sqrt(variance[i-1])*innovations[i-1] + lambda_param * variance[i]
    
filtered_variance = variance[1000:]
filtered_y = y[1000:]

#Exercise 6
z = np.zeros((5,5))
for i in np.arange(0, 5):
    for j in np.arange(0, 5):
        z[i,j] = i*j
#print(z)

#Exercise 7
def bisection_solve_cdf(x):
    minval = -5
    maxval = 5
    tolerance = 1e-6
    error_term = 1
    
    while abs(error_term) > tolerance:
        midval = (minval+maxval)/2
        mid_p = stats.norm.cdf(midval)
        error_term = mid_p - x
        if error_term > 0:
            maxval = midval
        else:
            minval = midval
            
    return midval
    
#Exercise 8
print(bisection_solve_cdf(0.01))
print(bisection_solve_cdf(0.5))
print(bisection_solve_cdf(0.975))

