# -*- coding: utf-8 -*-

'''
Created on 2017年12月3日
@author: Nick
'''

'''
   获取并可视化股票数据
'''

import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style

# 使用自带的样式进行美化
style.use('ggplot')

start = datetime.datetime(2017,1,1)
end = datetime.datetime(2017,12,1)

df = web.DataReader("XOM", "yahoo", start, end)

print(df.head())

df['Adj Close'].plot()

plt.show()
