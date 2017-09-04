# -*- coding: utf-8 -*-

'''
Created on 2017 年 9 月 4 日

@author: Nick
'''

'''
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
程序分析：请抓住分子与分母的变化规律。
'''

sum1 = 0
a, b = 1, 2
for i in range(1, 21):
    sum1 += b / a
    a, b = b, a + b
print(sum1)
