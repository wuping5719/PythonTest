# -*- coding: utf-8 -*-

'''
Created on 2017 年 9 月  15 日

@author: Nick
'''

'''
题目：学习使用auto定义变量的用法。
'''

num = 2
def autofunc():
    num = 1
    print ('Internal block num = %d' % num)
    num += 1
for i in range(3):
    print ('The num = %d' % num)
    num += 1
    autofunc()
