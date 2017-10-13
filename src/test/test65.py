# -*- coding: utf-8 -*-

'''
Created on 2017 年 10 月  13 日

@author: Nick
'''

'''
题目：找到年龄最大的人，并输出。
'''

if __name__ == '__main__':
    person = {"li":18, "wang":50, "zhang":20, "sun":22}
    m = 'li'
    for key in person.keys():
        if person[m] < person[key]:
            m = key
 
    print ('%s,%d' % (m,person[m]))
