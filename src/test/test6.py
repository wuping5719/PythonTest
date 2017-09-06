# -*- coding: utf-8 -*-

'''
Created on 2017 年 9 月 5 日

@author: Nick
'''

'''
题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....
'''

def rabbit(n):
    count = [1,0,0]  # 将兔子成长期分为三个月
    for i in range(1, n): # 每个月更新一次不同成长期的兔子对数
        count[2] = count[2] + count[1]
        count[1] = count[0]
        count[0] = count[2]
    return count[0]+count[1]+count[2] # 返回兔子对数总数

n = int(input("查看第几个月的兔子对数: "))
rabbit_sum = rabbit(n)
print("第%d个月的兔子对数为: %d" % (n,rabbit_sum))
