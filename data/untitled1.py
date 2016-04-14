# -*- coding: utf-8 -*-
#
# This prints a value from stocks before and after changing it to a float.
#
# %pylab inline
from yahoo_finance import Share
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
security = Share('IBM')
df = security.get_historical('2016-03-27', '2016-04-07')
table1 = pd.DataFrame(df)
stock = table1[['Low']]

print "Before changing type to float: ",stock.loc[0]
stock = stock.astype(float)
print "After changing type to float: ",stock.loc[0]
stock.plot()
