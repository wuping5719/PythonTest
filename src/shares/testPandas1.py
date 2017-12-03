# -*- coding: utf-8 -*-

'''
Created on 2017年12月2日
@author: Nick
'''

'''
   获取并可视化股票数据
   使用 pandas_datareader从雅虎财经获取数据
'''

import pandas_datareader.data as web   # 导入 Data 需要导入的包和模块
import datetime
 
# 从 2017年 1月 1日 开始过去一年的价格
start = datetime.datetime(2017,1,1)
end = datetime.datetime(2017,12,1)
 
# 得到苹果公司的股票数据，苹果公司的股票代码是 AAPL
# 第一个参数是要获取的股票代码；
# 第二个是源("yahoo"代表Yahoo财经),("google"代表谷歌财经) 
# 第三个是开始日期，第四个是结束日期.
# 雅虎, 谷歌数据源已经失效
apple = web.DataReader("AAPL", "yahoo", start, end) 

print(apple.head())
