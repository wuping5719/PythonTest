# -*- coding: utf-8 -*-

'''
Created on 2017 年 9 月  12 日

@author: Nick
'''

'''
题目：利用递归方法求5!。
程序分析：递归公式：fn=fn_1*4!
'''

def fun(n):
    if n==1 or n==0:
        return 1
    else:
        return fun(n-1)*n

print (fun(4))
