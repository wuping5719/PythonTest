'''
Created on 2018年3月30日
@author: WuPing
'''

from numpy import *
import operator
from os import listdir

from math import log

def createDataSet():    # 简单鉴定数据集
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing','flippers']
    # change to discrete values
    return dataSet, labels

def calcShannonEnt(dataSet):    # 计算给定数据集的香农熵
    numEntries = len(dataSet)   # 计算数据集中的实例总数
    labelCounts = {}  # 创建数据字典，其键值是最后一列的数值
    for featVec in dataSet: # the the number of unique elements and their occurance  
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys(): 
            labelCounts[currentLabel] = 0    # 如果当前键值不存在，则扩展字典并将当前键值加入字典
            labelCounts[currentLabel] += 1   # 每一个键值都记录了当前类别的次数
    # 使用所有类标签发生的频率计算类别出现的概率，计算香农熵
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob,2) # log base 2
    return shannonEnt

# reload(trees)
myDat, labels = createDataSet()
print(myDat)

print(calcShannonEnt(myDat))
