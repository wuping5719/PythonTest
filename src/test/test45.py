# -*- coding: utf-8 -*-

'''
Created on 2017 年 9 月  16 日

@author: Nick
'''

'''
题目：学习使用按位异或 ^ 。
程序分析：0^0=0; 0^1=1; 1^0=1; 1^1=0
'''

if __name__ == '__main__':
    a = 77
    b = a ^ 3
    print ('The a ^ 3 = %d' % b)
    b ^= 7
    print ('The a ^ b = %d' % b)
