# -*- coding: utf-8 -*-

'''
Created on 2017 年 9 月  11 日

@author: Nick
'''

'''
打印出如下图案（菱形）:
   *
  ***
 *****
*******
 *****
  ***
   *
程序分析：先把图形分成两部分来看待，前四行一个规律，后三行一个规律，
利用双重for循环，第一层控制行，第二层控制列。
'''
                      
def pic(lines):    
    middle, lines = int(lines / 2), int(lines / 2) * 2 + 1    
    for i in range(1, lines + 1):        
        empty = abs(i - middle - 1)        
        print(' ' * empty, '*' * (2 * (middle - empty) + 1))
line = 7 # 设置输出行数
pic(7)
