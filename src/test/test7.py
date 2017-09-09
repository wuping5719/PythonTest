# -*- coding: utf-8 -*-

'''
Created on 2017 年 9 月 9 日

@author: Nick
'''

'''
题目：判断101-200之间有多少个素数，并输出所有素数。

程序分析：判断素数的方法：用一个数分别去除  2 到 sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。 
'''

list1 = []
list2 = []
for x in range(2, 101):
    for i in range(2, x+1):
        sum1 = x * i
        if (sum1 < 200) & (sum1 > 101):
            list1.append(sum1)
for m in range(101, 200):
    list2.append(m)
list3 = list(set(list2) ^ set(list1))
print(list1, '\n')
print(list3)
print("总数为：", len(list3))
