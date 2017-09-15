# -*- coding: utf-8 -*-

'''
Created on 2017 年 9 月  14 日

@author: Nick
'''

'''
题目：求100之内的素数。
'''

# 用户输入数据
lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))
 
for num in range(lower,upper + 1):
    # 素数大于 1
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)
