# -*- coding: utf-8 -*-

'''
Created on 2017年12月3日
@author: Nick
'''

'''
 Python股市数据分析教程: 
   http://blog.yhat.com/posts/stock-data-python.html
   http://blog.csdn.net/xiao_lxl/article/details/53780988
   获取并可视化股票数据
'''
import pandas as pd
import pandas_datareader.data as web   # 导入 Data 需要导入的包和模块
import datetime

start = datetime.datetime(2017,1,1)
end = datetime.datetime(2017,12,1)

apple = web.DataReader("AAPL", "yahoo", start, end) 
microsoft = web.DataReader("MSFT", "yahoo", start, end)
google = web.DataReader("GOOG", "yahoo", start, end)

stocks = pd.DataFrame({"AAPL": apple["Adj Close"],
                      "MSFT": microsoft["Adj Close"],
                      "GOOG": google["Adj Close"]})

stocks.head()
# stocks.plot(grid = True)
stocks.plot(secondary_y = ["AAPL", "MSFT"], grid = True)
