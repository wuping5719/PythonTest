# -*- coding: utf-8 -*-

'''
Created on 2017 年 9 月  12 日

@author: Nick
'''

'''
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
程序分析：请抓住分子与分母的变化规律。
'''

# 方法一                   
a = 2
b = 1
lst = []
for i in range(20):
    lst.append(str(a) + '/' + str(b))
    a,b = a+b, a
print('{0} = {1}'.format(eval('+'.join(lst)), '+'.join(lst)))

# 方法二
sum1 = 0
a1, b1 = 1, 2
for i in range(1, 21):
    sum1 += b1 / a1
    a1, b1 = b1, a1 + b1
print(sum1)
