# -*- coding: utf-8 -*-

'''
Created on 2017 年 10 月  15 日

@author: Nick
'''

'''
题目：时间函数。
'''

if __name__ == '__main__':
    import time
    print (time.ctime(time.time()))
    print (time.asctime(time.localtime(time.time())))
    print (time.asctime(time.gmtime(time.time())))
