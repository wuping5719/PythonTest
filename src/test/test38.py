# -*- coding: utf-8 -*-

'''
Created on 2017 年 9 月  16 日

@author: Nick
'''

'''
题目：求输入数字的平方，如果平方运算后小于 50 则退出。
'''

def power(x):
    if x ** 2 >= 50:
        print('{}的平方为:{},不小于50，继续.'.format(x, x ** 2))
    else:
        print('{}的平方为:{},小于50，退出.'.format(x, x ** 2))
        quit()
while True:
    x = int(input('输入数字:'))
    power(x)
