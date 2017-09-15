# -*- coding: utf-8 -*-

'''
Created on 2017 年 9 月  14 日

@author: Nick
'''

'''
题目：对10个数进行排序。
程序分析：可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，
下次类推，即用第二个元素与后8个进行比较，并进行交换。
'''

import random
A = []
for i in range(10):
    A.append(random.randint(0,100))

print(A)
x = A
for i, j in enumerate(x):
    T = x[i+1:]
    if T == []:
        break

    if x[i] > min(T):
        t = x.index(min(T))
        x[i], x[t] = x[t], x[i]
print(A)
