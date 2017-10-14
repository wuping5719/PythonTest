# -*- coding: utf-8 -*-

'''
Created on 2017 年 10 月  14 日

@author: Nick
'''

'''
题目：求0—7所能组成的奇数个数。
程序分析：
组成1位数是4个。
组成2位数是7*4个。
组成3位数是7*8*4个。
组成4位数是7*8*8*4个。
'''

if __name__ == '__main__':
    sum1 = 4
    s = 4
    for j in range(2,9):
        print (sum1)
        if j <= 2:
            s *= 7
        else:
            s *= 8
        sum1 += s
    print ('sum = %d' % sum1)
