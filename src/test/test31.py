# -*- coding: utf-8 -*-

'''
Created on 2017 年 9 月  16 日

@author: Nick
'''

'''
题目：求一个3*3矩阵对角线元素之和。
程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。
'''

"""
   1  2  3
   4  5  6 
   7  8  9
"""
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum_ = 0
for i in range(0, 3):
    sum_ += matrix[i][i]
print (sum_)
