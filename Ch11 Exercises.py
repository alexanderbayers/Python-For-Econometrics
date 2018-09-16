#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 15:53:47 2018

@author: alexanderbayers
"""

import numpy as np

#Exercise 1
loadtextversion = np.loadtxt('/Users/alexanderbayers/Downloads/exercise3.csv', delimiter = ',', skiprows = 1)
dates = loadtextversion[:,0]
XOM = loadtextversion[:,1]
SPX = loadtextversion[:,2]
sum(XOM > 0)
sum(SPX > 0)


SPX_2sd = np.logical_or((SPX > (np.mean(SPX) + 2*np.std(SPX))),  (SPX < (np.mean(SPX) - 2*np.std(SPX))))
np.mean(SPX[SPX_2sd])
np.std(SPX[SPX_2sd])
XOM_2sd = np.logical_or((XOM > (np.mean(XOM) + 2*np.std(XOM))),  (XOM < (np.mean(XOM) - 2*np.std(XOM))))
np.mean(XOM[XOM_2sd])
np.std(XOM[XOM_2sd])
#The mean return for the SPX is -30 bps.
#The mean return for the XOM is -20 bps.

#Exercise 3
np.corrcoef(XOM, SPX)
#The unconditional correlation is .592
#Conditional on one being less than 0, the correlation coefficient is .32
#Conditional on both being less than 0, the correlation coefficient is .62

