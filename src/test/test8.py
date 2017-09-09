# -*- coding: utf-8 -*-

'''
Created on 2017 年 9 月 9 日

@author: Nick
'''

'''
题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
           例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。
'''

a = 1
b = 1
c = 1
for a in range(0,10):
    for b in range(0,10):
        for c in range(0,10):
            if int(a)**3+int(b)**3+int(c)**3 == a*100+b*10+c and a != 0:
                x = a*100+b*10+c
                print(x)
