# -*- coding: utf-8 -*-

'''
Created on 2017 年 8 月 28 日

@author: Nick
'''

# 用户输入数字
num1 = input('输入第一个数字：')
num2 = input('输入第二个数字：')

# 求和
sum1 = float(num1) + float(num2)

# 显示计算结果
print('数字 {0} 和 {1} 相加结果为： {2}'.format(num1, num2, sum1))

num = float(input('请输入一个数字： '))
num_sqrt = num ** 0.5
print(' %0.3f 的平方根为 %0.3f'%(num ,num_sqrt))

import cmath
 
num = int(input("请输入一个数字: "))
num_sqrt = cmath.sqrt(num)
print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))

# 二次方程式 ax**2 + bx + c = 0
# a、b、c 用户提供

a = float(input('输入 a: '))
b = float(input('输入 b: '))
c = float(input('输入 c: '))

# 计算
d = (b**2) - (4*a*c)

# 两种求解方式
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('结果为 {0} 和 {1}'.format(sol1,sol2))
