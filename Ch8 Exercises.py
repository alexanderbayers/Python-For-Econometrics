#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 23:40:11 2018

@author: alexanderbayers
"""

import numpy as np

#Exercise 1
x = np.arange(12)
x.shape = (1, 12)
x.shape = (2, 6)
x.shape = (3, 4)
x.shape = (4, 3)
x.shape = (6, 2)
x.shape = (2,2, 3)
x.shape = 12

#Using reshape
x.reshape(1, 12)
x.reshape(2, 6)
x.reshape(3, 4)
x.reshape(4, 3)
x.reshape(6, 2)
x.reshape(2,2, 3)
x.reshape(12)
           
#Exercise 2
num_array = np.array([1, 3, 5, 7, 9, 11])
x.ravel()[num_array]
x.flatten()[num_array]
x.flat[num_array]

#Exercise 3
x = np.tile(1, (2, 2))
y = np.tile(2, (1, 1))
z = np.tile(3, (3, 2))
w = np.hstack((np.vstack((x, z)), np.vstack((np.tile(y, (2, 3)), z.T, np.tile(y, (1, 3))))))

#Exercise 4
x = np.reshape(np.arange(12.0),(2,2,3))
x.squeeze()
y = x.squeeze()
np.shape(x)
np.shape(y)
#It does nothing

#Exercise 5
y = np.array([[2, .5], [.5, 4]])
z = np.diag(np.diag(y))

#Exercise 6
np.linalg.cholesky(y)
np.dot(np.linalg.cholesky(y), np.linalg.cholesky(y).T)

#Exercise 7
np.linalg.det(y)
val, vec = np.linalg.eig(y)
val[1]*val[0]
np.matrix.trace(y)
sum(val)

#Exercise 8
np.dot(vec, np.dot(np.linalg.inv(np.diag(val)),vec.T))
np.linalg.inv(y)

#Exercise 9
x = np.random.randn(100, 2)
e = np.random.randn(100, 1)
B = np.array([[1],[0.5]])
y = np.dot(x, B) + e
np.linalg.lstsq(x,y)

#Exercise 10
y = np.array([[5, -1.5, -3.5], [-1.5, 2, -0.5], [-3.5, -.5, 4]])
np.linalg.matrix_rank(y)
val, vec = np.linalg.eig(y)
np.linalg.det(y)
#one of the eignevalues is 0 which accords with the matrix rank being zero

#Exercise 11
x = np.random.randn(100, 2)
np.kron(np.identity(2), np.cov(x.T))
