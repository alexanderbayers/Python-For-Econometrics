#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 23:24:07 2018

@author: alexanderbayers
"""

import numpy as np

#Exercise 1
u = np.array([1, 1, 2, 3, 5, 8])
umat = np.asmatrix(u)

v =np.array([[1],[1],[2],[3],[5],[8]])
vmat = np.asmatrix(v)

x = np.array([[1.0, 0], [0, 1]])
xmat = np.asmatrix(x)

y = np.reshape(np.arange(1, 5), (2,2))
ymat = np.matrix(y)

z = np.hstack((np.vstack((y, np.array([1, 2]))), np.vstack((y, np.array([1, 2])))))
zmat = np.matrix(z)

w = np.vstack((np.hstack((x, x)), np.hstack((y, y))))
wmat = np.matrix(w)

#Ex 1
print(u + v.T)
print(v + u.T)
print(np.dot(v, [u]))
print(np.dot(u,v))
print(np.dot(x, y))

#Ex2
print(umat+vmat.T)
print(vmat + umat.T)
print(vmat*umat)
print(umat*vmat)
print(xmat*ymat)

#Ex3
a = np.array([3, 2])
b = np.array([[3], [2]])
c = np.arange(3, -1, -1)
d = np.reshape(np.arange(3, -1, -1), (4, 1))

#Arrays v, x, y can be added to array a
#b can add arrays u, x, y
#c can ad arrays v, z, w
#d can add arrays u, w

#Ex4
#x /1 is legal.  1/x isn't legal because you're dividing by 0

#Ex5
#They are the same if using arrays, and they are the same if they are matrices

#Ex6
#They are the same as the above

#Ex7
#They are not guaranteed to be the same

#Ex8
#its not.  Instead, we need to add parentheses so its a*(b+c)

#Ex9
#y needs to be a scalar.  
#x and w must be the same dimension


#Exercise 10
#First is -16, the others are positivie 16
