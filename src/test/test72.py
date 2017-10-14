# -*- coding: utf-8 -*-

'''
Created on 2017 年 10 月  14 日

@author: Nick
'''

'''
题目：输入一个正整数，然后判断最少几个 9 除于该数的结果为整数。
程序分析：999999 / 13 = 76923。
'''

if __name__ == '__main__':
    zi = int(input('输入一个数字:\n'))
    n1 = 1
    c9 = 1
    m9 = 9
    sum1 = 9
    while n1 != 0:
        if sum1 % zi == 0:
            n1 = 0
        else:
            m9 *= 10
            sum1 += m9
            c9 += 1
    print ('%d 个 9 可以被 %d 整除 : %d' % (c9,zi,sum1))
    r = sum1 / zi
    print ('%d / %d = %d' % (sum1,zi,r))
