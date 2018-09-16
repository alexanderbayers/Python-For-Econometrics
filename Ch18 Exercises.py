#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 22:21:19 2018

@author: alexanderbayers
"""

import numpy as np

#Exercise 1
def unique_values(array):
    
    """Takes an array, and returns an array of the location of the arrays.  Then returns an 
    array of the individual unique vaues"""
    
    unique_array  = np.unique(array)
    array_shaped = np.zeros((array.shape[0],unique_array.shape[0]))
    
    for value_counter in np.arange(0, len(array)):
        array_shaped[value_counter, np.where(unique_array == array[value_counter])[0][0]] = 1
            
    return array_shaped, unique_array
    

#z = unique_values(np.array([1, 2, 1, 1, 2]))

#Exercise 2
def gls(X, y, Omega = None):
    
    """Takes a dependent T x k matrix X,an independent matrix y, and a covariance matrix Omega
    (assumed to be the identity if nothing) and returns the gls estimate
    """
    
    if Omega is None:
        Omega = np.identity(X.shape[0])
    
    Beta = np.dot(np.linalg.inv(np.dot(np.dot(X.T, np.linalg.inv(Omega)),X)), \
                        np.dot(X.T, np.dot(np.linalg.inv(Omega),y)))
    return Beta

#TODO Exercise 3