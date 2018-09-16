#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 10:03:18 2018

@author: alexanderbayers
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import scipy.io as sio

#Exercise 2
loadtextversion = np.loadtxt('/Users/alexanderbayers/Downloads/exercise3.csv', delimiter = ',', skiprows = 1)
readcsvversion = pd.read_csv('/Users/alexanderbayers/Downloads/exercise3.csv', index_col = 'Date')
gentextversion = np.genfromtxt('/Users/alexanderbayers/Downloads/exercise3.csv', delimiter = ',')
csv2recversion = mpl.mlab.csv2rec('/Users/alexanderbayers/Downloads/exercise3.csv', delimiter = ',')

#Exercise 3
dates = loadtextversion[:,0]
XOM = loadtextversion[:,1]
SPX = loadtextversion[:,2]

#Exercise 4
np.savez('/Users/alexanderbayers/Downloads/test_uncompressed.npz', dates = dates, XOM = XOM, PSX = SPX)
np.savez_compressed('/Users/alexanderbayers/Downloads/test_compressed.npz', dates = dates, XOM = XOM, PSX = SPX)
saveData = {'dates': dates, 'SPX' : SPX, 'XOM' : XOM}
sio.savemat('/Users/alexanderbayers/Downloads/test',saveData,do_compression=True)
#Matlab file is the smallest

#Exercise 5
sumreturns = XOM + SPX
outputdata = np.hstack((dates, sumreturns))
np.savetxt('/Users/alexanderbayers/Downloads/outputdata.csv',outputdata.T, delimiter = ',')