# -*- coding: utf-8 -*-

'''
Created on 2017 年 9 月  16 日

@author: Nick
'''

'''
题目：两个变量值互换。
'''

def exchange(a,b):
    a,b = b,a
    return (a,b)
 
if __name__ == '__main__':
    x = 10
    y = 20
    print ('x = %d,y = %d' % (x,y))
    x,y = exchange(x,y)
    print ('x = %d,y = %d' % (x,y))
