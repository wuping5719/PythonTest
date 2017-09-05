# -*- coding: utf-8 -*-

'''
Created on 2017 年 9 月 5 日

@author: Nick
'''

'''
题目：暂停一秒输出，并格式化当前时间。
'''

import time, datetime

TIME1 = datetime.datetime.now()

print(TIME1.strftime("%Y-%m-%d %H:%M:%S"))

time.sleep(1)

TIME2 = datetime.datetime.now()

print(TIME2.strftime("%Y-%m-%d %H-%M-%S"))
