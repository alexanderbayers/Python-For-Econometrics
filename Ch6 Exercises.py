#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 00:12:13 2018

@author: alexanderbayers
"""

import numpy as np

#Exercise 1
#Replicating [0, ..., 10]
#Using linspace
np.linspace(0, 10, 11)
#Using aragne
np.arange(0, 11, 1)
#Using r
np.r_[0:11:1]


#Using linspace
np.linspace(4, 13, 10)
#Using aragne
np.arange(4, 14, 1)
#Using r
np.r_[4:14:1]

#Using linspace
np.linspace(0, 1, 5)
#Using aragne
np.arange(0, 1.25, .25)
#Using r
np.r_[0:1.25:.25]

#Using linspace
np.linspace(0, -5, 6)
#Using aragne
np.arange(0, -6, -1)
#Using r
np.r_[0:-6:-1]

#Exercise 2
np.logspace(0,2,21) == 10**np.linspace(0,2,21)
np.linspace(2,10,51) == np.log10(np.logspace(2,  10, 51))

#Exercise 3
y = [0, 0.5, 1.5, 2.5, 1.0, 1.0001,-0.5,-1,-1.5,-2.5]
np.round(y)
np.floor(y)
np.ceil(y)

#Exercise 4
to_sum = np.arange(0, 11, 1)
np.cumsum(to_sum)
(np.arange(0, 11)*(np.arange(0, 11)+1))/2 == np.cumsum(to_sum)

#Exercise 5
x = np.random.randn(20)
#They are only equal for the last element

#Exercise 6
#Its reversed and msising the last element

#Exercise 7
y = np.array([np.log(0.5), np.log(1), np.log(np.e) ])
np.e ** y

#Exercise 8
np.absolute(np.array([0, -3.14, 3+4j]))

#Exercise 9
#x.sort changes it in place, whereas y = np.sort(x) does it on a copy and leaves the original unchanged

#Exercise 10
x[np.argmax(x)]
x.max()


#Exercsie 11
np.setdiff1d(x, y)
x[np.in1d(x, y) == False]

#Exercise 12
y = [np.nan, 2.2, 3.9, 4.6, np.nan, 2.4, 6.1, 1.8]
variance = (np.nansum((y - np.nansum(y)/sum(1-np.isnan(y))) ** 2))/(sum(1-np.isnan(y)))