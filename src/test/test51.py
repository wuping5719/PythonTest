# -*- coding: utf-8 -*-

'''
Created on 2017 年 9 月  17 日

@author: Nick
'''

'''
题目：打印出杨辉三角形。
'''

def Pascal(n):
    ls = [[1]]
    for i in range (1, n):
        ls.append([1])
        for j in range(1, i):
            ls[i].append(ls[i-1][j-1] + ls[i-1][j])
        ls[i].append(1)
    for i in range(0, n): print(ls[i])
    return ls

a = Pascal(10)
