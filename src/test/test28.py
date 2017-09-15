# -*- coding: utf-8 -*-

'''
Created on 2017 年 9 月  14 日

@author: Nick
'''

'''
题目：函数调用。
'''

def hello_world(i):
    print ('hello world')

def three_hellos():
    for i in range(3):
        hello_world(i)
if __name__ == '__main__':
    three_hellos()
