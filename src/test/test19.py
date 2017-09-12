# -*- coding: utf-8 -*-

'''
Created on 2017 年 9 月  12 日

@author: Nick
'''

'''
题目：求1+2!+3!+...+20!的和。
程序分析：此程序只是把累加变成了累乘。
'''

# 方法一                   
s = 0
for i in range(1, 21):
    r = 1
    for j in range(1, i+1):
        r *= j
    s += r
print(s)

# 方法二
def jiecheng(n):
    if n==1:
        return 1
    else:
        return n*jiecheng(n-1)

def sum1(n):
    if n==1:
        return jiecheng(1)
    else:
        return jiecheng(n)+sum1(n-1)

print(sum1(20))
