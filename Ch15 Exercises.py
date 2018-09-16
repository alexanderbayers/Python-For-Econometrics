#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 20:03:41 2018

@author: alexanderbayers
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import scipy.stats as stats
import seaborn as sns
import matplotlib.dates as mdates
import statsmodels.api as sm
import math

mpl.rcParams['axes.autolimit_mode'] = 'round_numbers'
mpl.rcParams['axes.xmargin'] = 0
mpl.rcParams['axes.ymargin'] = 0

#Exercise 1
#Set environment
sns.set(style='darkgrid')

ftse_data = pd.read_csv('/Users/alexanderbayers/Downloads/FTSE 100 Historical Data.csv', thousands = ',')
spx_data = pd.read_csv('/Users/alexanderbayers/Downloads/S&P 500 Historical Data.csv', thousands = ',')

ftse_data['Date'] = pd.to_datetime(ftse_data['Date'],infer_datetime_format=True)
spx_data['Date'] = pd.to_datetime(spx_data['Date'],infer_datetime_format=True)
spx_data.set_index('Date', inplace = True)
ftse_data.set_index('Date', inplace = True)


#plt.autoscale(axis='x')
#plt.tight_layout()

months = mdates.MonthLocator(interval = 6)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.xaxis.set_major_locator(months)
fmt = mdates.DateFormatter('%b %y')
ax.plot(spx_data['Price'])
fig.autofmt_xdate()
ax.xaxis.set_major_formatter(fmt)

numbins = 40
spx_data['Log_price'] = np.log(spx_data['Price'])
spx_data_resample = spx_data.resample('W-FRI', closed = 'right').last()
spx_data_resample['Log_price'].diff().dropna()
plt.hist(spx_data_resample['Log_price'].diff().dropna(), bins = numbins)

#Exercise 3 Convert the data to log returns and cut 
log_returns = pd.DataFrame(spx_data_resample['Log_price'].diff().dropna())
labels = ['r <= - 2%', '-2% < r <= 0%', '0% < r <= 2%', 'r > 2%']
log_returns['bins'] = pd.cut(log_returns['Log_price'], bins = [-1, -.02, 0, .02, 1], \
           labels = labels)
#wedges = plt.pie(log_returns.groupby('bins').count()/len(log_returns), autopct = '%1.1f%%', labels= labels)


#Exercise 4
log_returns = pd.DataFrame(spx_data_resample['Log_price'].diff().dropna())
log_returns.rename(columns = {'Log_price': 'SPX'}, inplace = True)
ftse_data['Log_price'] = np.log(ftse_data['Price'])
ftse_data_resample = ftse_data.resample('W-FRI', closed = 'right').last()
ftse_log_returns = pd.DataFrame(ftse_data_resample['Log_price'].diff().dropna()).rename(columns = {'Log_price':'FTSE 100'})
log_returns = log_returns.join(ftse_log_returns, how ='inner')

plt.title('FTSE 100 ~ SPX')
plt.xlabel('SPX')
plt.ylabel('FTSE 100')
plt.scatter(log_returns['SPX'], log_returns['FTSE 100'])

#Fit a amodel
model = sm.OLS(log_returns['FTSE 100'], sm.add_constant(log_returns['SPX'])).fit()
X_plot = np.linspace(-.25,.2,100)
plt.plot(X_plot, X_plot*model.params[1] + model.params[0])
plt.autoscale(axis='x')
plt.show()


#Example 7
log_returns['SPX Squared'] = log_returns['SPX'] ** 2
log_returns['FTSE 100 Squared'] = log_returns['FTSE 100'] ** 2
log_returns['SPX Variance'] = None
log_returns['FTSE Variance'] = None
lambda_coef = .97
for i in np.arange(0, log_returns.shape[0]):
    if i == 0:
        log_returns.loc[log_returns.index[i], 'SPX Variance'] = log_returns['SPX Squared'].mean()
        log_returns.loc[log_returns.index[i], 'FTSE Variance'] = log_returns['FTSE 100 Squared'].mean()
    else:
        log_returns.loc[log_returns.index[i], 'SPX Variance'] = lambda_coef * log_returns.loc[log_returns.index[i-1], 'SPX Variance'] + \
                       (1-lambda_coef) * log_returns.loc[log_returns.index[i-1], 'SPX Squared']
        log_returns.loc[log_returns.index[i], 'FTSE Variance'] = lambda_coef * log_returns.loc[log_returns.index[i-1], 'FTSE Variance'] + \
                       (1-lambda_coef) * log_returns.loc[log_returns.index[i-1], 'FTSE 100 Squared']
plt.plot(log_returns['SPX Variance'], label = 'SPX Variance')
plt.plot(log_returns['FTSE Variance'], label = 'FTSE Variance')
plt.legend()

    
    