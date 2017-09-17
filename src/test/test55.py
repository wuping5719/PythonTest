# -*- coding: utf-8 -*-

'''
Created on 2017 年 9 月  17 日

@author: Nick
'''

'''
题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
'''

from collections import deque

m = 3
a = [1,2,3,4,5,6,7]   # 7 个数
f = deque(a)
f.rotate(m)
print (list(f))
