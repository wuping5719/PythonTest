# -*- coding: utf-8 -*-

'''
Created on 2017 年 9 月 9 日

@author: Nick
'''

'''
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
(1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
(2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
(3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。
'''

def prime(n):
    l = []
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n = int(n / i)
                l.append(i)
                break    
    return l


s = input("输入一个正整数:")
if s.isdigit() and int(s) > 0:
    print(s, "=", "*".join([str(x) for x in prime(int(s))]))
else:
    print("请输入正确的正整数.")
