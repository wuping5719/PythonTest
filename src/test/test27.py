# -*- coding: utf-8 -*-

'''
Created on 2017 年 9 月  14 日

@author: Nick
'''

'''
题目：按逗号分隔列表。
'''

# 方法一
l = [1,2,3,4,5,6,7];
o = '';
for i in l:
    o += str(i)+',';
print(o[0:-1]);
