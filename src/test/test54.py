# -*- coding: utf-8 -*-

'''
Created on 2017 年 9 月  17 日

@author: Nick
'''

'''
题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
'''

a=[1,2,3,7,9,8]
for i in range(len(a)):
    if a[i]==max(a):
        a[0],a[i]=a[i],a[0]

for i in range(len(a)):
    if a[i]==min(a):
        a[len(a)-1],a[i]=a[i],a[len(a)-1]

print (a)
