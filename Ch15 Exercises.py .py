#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 20:03:41 2018

@author: alexanderbayers
"""

import pandas as pd
import numpy as np


ftse_data = np.loadtxt('/Users/alexanderbayers/Downloads/FTSE 100 Historical Data.csv', delimiter = ',', skiprows = 1)
spx_data = np.loadtxt('/Users/alexanderbayers/Downloads/S&P 500 Historical Data.csv', delimiter = ',', skiprows = 1)