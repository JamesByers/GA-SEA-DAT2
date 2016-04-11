# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 13:01:08 2016

@author: jim_byers
"""
from yahoo_finance import Share
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# %pylab inline
security = Share('IBM')
df = security.get_historical('2016-03-27', '2016-04-07')
table1 = pd.DataFrame(df)
stock = table1[['Low']]
​
stock.plot()
