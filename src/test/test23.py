# -*- coding: utf-8 -*-

'''
Created on 2017 年 9 月  13 日

@author: Nick
'''

'''
题目：给一个不多于5位的正整数，要求：
一、求它是几位数，
二、逆序打印出各位数字。

'''

num=int(input("请输入一个正整数:"))
def fn(s):
    if len(s)==1:
        return(s[0])
    else:
        a=s[-1]
        s=s[:-1]
        return(a+fn(s))

while 1:
    if num<=0 or len(str(num))>5:
        num=int(input("输入错误，请重新输入:"))
    else:
        num=str(num)
        print()
        print("它是%d位数" % len(num))
        print("逆序打印:",fn(num))
        break
