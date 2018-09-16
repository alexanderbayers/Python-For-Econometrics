#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 09:20:23 2018

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

#Exercise 2
#Option 1
w[0:2, 0:2]

#Option 2
w[0:2, 2:4]

#Exercise 3
#Option 1
w[:, :2]

#Option 2
w[:, 2:]

#Exercise 4
#Option 1
z[:2,:2]

#Option 2
z[:2,2:]

#Exercise 6
f = [1.6180,  2.7182, 3.1415]
np.mat(f)