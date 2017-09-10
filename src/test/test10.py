# -*- coding: utf-8 -*-

'''
Created on 2017 年 9 月 9 日

@author: Nick
'''

'''
题目：输出指定格式的日期。

程序分析：使用 datetime 模块。
'''

import datetime
 
if __name__ == '__main__':
 
    # 输出今日日期，格式为yyyy-mm-dd。更多选项可以查看 strftime() 方法
    print(datetime.date.today().strftime('%Y-%m-%d'))
 
    # 创建日期对象
    nickBirthDate = datetime.date(1990, 9, 8)
 
    print(nickBirthDate.strftime('%Y-%m-%d'))
 
    # 日期算术运算
    nickBirthNextDay = nickBirthDate + datetime.timedelta(days=1)
 
    print(nickBirthNextDay.strftime('%Y-%m-%d'))
 
    # 日期替换
    nickFirstBirthday = nickBirthDate.replace(year=nickBirthDate.year + 1)
 
    print(nickFirstBirthday.strftime('%Y-%m-%d'))
