# -*- coding: utf-8 -*-

'''
Created on 2017 年 9 月  10 日

@author: Nick
'''

'''
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

程序分析：关键是计算出每一项的值。
'''

n = int(input('n = '))
a = int(input('a = '))
sum1 = 0
total = 0
for i in range(n):
    sum1 += (10 ** i)
    total += sum1 * a
print(total)
