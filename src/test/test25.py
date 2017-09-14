# -*- coding: utf-8 -*-

'''
Created on 2017 年 9 月  13 日

@author: Nick
'''

'''
题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
'''

weeklist = {'M': 'Monday','T': {'u': 'Tuesday','h':'Thursday'}, 
            'W': 'Wednesday', 'F':'Friday',
            'S':{'a':'Saturday','u':'Sunday'}}
sLetter1 = input("请输入首字母：")
sLetter1 = sLetter1.upper()

if (sLetter1 in ['T','S']):
    sLetter2 = input("请输入第二个字母：")
    print(weeklist[sLetter1][sLetter2])
else:
    print(weeklist[sLetter1])
