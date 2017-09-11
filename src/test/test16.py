# -*- coding: utf-8 -*-

'''
Created on 2017 年 9 月  11 日

@author: Nick
'''

'''
题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。
有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
'''
                      
n=['a','b','c']
m=['x','y','z']
L=[]
for i in range(0,3):
    for j in range(0,3):
        L.append(n[i]+'-'+m[j])
L.remove('a-x')
L.remove('a-y')
L.remove('b-y')
L.remove('b-z')
L.remove('c-x')
L.remove('c-z')
print(L)
