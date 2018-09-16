#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 22:55:22 2018

@author: alexanderbayers
"""

import numpy as np

#Exercise 1
zeros = np.zeros((10, 5))
ones = np.ones((10, 5))

#Exercise 2
zeros * ones

#Exercise 3
np.identity(5)

#Exercise 4
newzeros = np.tile(0, (10, 5))
newones = np.tile(1, (10, 5))

#Exercise 5
np.diag(np.diag(np.ones((3,3))))

#Exercise 6
y=np.empty((1,))
y10 = np.empty((10,))
#Different values