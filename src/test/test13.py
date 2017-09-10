# -*- coding: utf-8 -*-

'''
Created on 2017 年 9 月  10 日

@author: Nick
'''

'''
题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。
例如6=1＋2＋3.编程找出1000以内的所有完数。
'''

list2 = []
for x in range(1, 1001):
    list1 = []
    for i in range(1, int(x / 2) + 1):
        if x % i == 0:
            list1.append(i)
    if x == sum(list1):
        print(x)
        print(list1)
        list2.append(x)
        print("共计有%d个完数"%(len(list2)))
