# -*- coding: utf-8 -*-

'''
Created on 2017 年 10 月  13 日

@author: Nick
'''

'''
题目：判断情人节。
'''

import time

if __name__=='__main__':
    date=time.strftime('%m-%d',time.localtime())
    if date=='02-14':
        print ('情人节是时候给你女朋友买支玫瑰花了！！')
    else:
        print ('这时候你不要忘记发个红包！！')
        
    for i in range(5):
        n = 0
        if i != 1: n += 1
        if i == 3: n += 1
        if i == 4: n += 1
        if i != 4: n += 1
        if n == 3: print (64 + i)
