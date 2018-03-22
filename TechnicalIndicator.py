# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import talib as ta
import matplotlib.pyplot as plt

# AUD/JPY historical data(csv file)
filename = 'AUDJPY.csv'

# csv -> DataFrame
# - index_col='日付': indexとしてhistorical dataの'日付'columnを使用するため
# - encoding='cp932': historical dataの日本語のcodeを正しく処理するため
df = pd.read_csv(filename, index_col='日付', encoding='cp932')

# DataFrame -> array
closing = np.array(df['終値'])

output = closing.copy()
cols = ['Closing']

output = np.c_[output, ta.SMA(closing)] # concatination
cols += ['SAM']
output = np.c_[output, ta.WMA(closing)] # concatination
cols += ['WMA']
output = np.c_[output, ta.EMA(closing)] # concatination
cols += ['EMA']
for arr in ta.MACD(closing):
    output = np.c_[output, arr]
cols += ['MACD', 'MACD_signal', 'MACD_hist']


# Create DataFrame
# - index=df.index: 元々はhistorical dataの'日付'column
# - columns=cols: output作成時に本dataを同時に作成
data = pd.DataFrame(output, index=df.index, columns=cols)
data.tail()

data.plot()
plt.savefig("AUDJPY_ta.png")
plt.show()

data.to_csv('AUDJPY_ta.csv')
                
