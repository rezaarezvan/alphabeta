# Importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import warnings

warnings.filterwarnings("ignore")

# is used to fetch data 
import yfinance as yf
yf.pdr_override()

# input
ticker = "NFLX"
spx = "^GSPC"
start = '2020-01-01'
end = '2022-08-17'

# Read data 
stock = yf.download(ticker,start,end)
market = yf.download(spx, start, end)
prices = stock['Adj Close']
values = market['Adj Close']
ret = (np.log(prices) - np.log(prices.shift(1))).dropna()
mrk = values.pct_change(1).dropna()
beta, alpha, r_value, p_value, std_err = stats.linregress(ret, mrk)

print("Beta: 			%9.6f" % beta)
print("Alpha: 			%9.6f" % alpha)
print("R-Squared: 		%9.6f" % r_value)
print("p-value: 		%9.6f" % p_value)
print("Standard Error: 	%9.6f" % std_err)