# -*- coding: utf-8 -*-

'''
Created on 2017 年 9 月 5 日

@author: Nick
'''

'''
题目：斐波那契数列。

程序分析：斐波那契数列（Fibonacci sequence），
又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
'''

class Fibs:
    def __init__(self, n = 10):
        self.a = 0
        self.b = 1
        self.n = n
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        self.i += 1
        if self.i > self.n:
            raise StopIteration
        return self.a
    
fibs = Fibs(10)

for i in fibs:
    print (i)
