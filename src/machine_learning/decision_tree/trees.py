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
print("\n")

print(calcShannonEnt(myDat))
print("\n")

def splitDataSet(dataSet, axis, value):
    # 创建新的 list 对象
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]   # chop out axis used for splitting
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

retDataSet = splitDataSet(myDat, 1, 0)
print(retDataSet)
print("\n")

def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1      # the last column is used for the labels
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0; bestFeature = -1
    # tableVocabulary = {}
    # print("baseEntropy = " + str(baseEntropy))
    for i in range(numFeatures):           # iterate over all the features
        # (以下两行)创建唯一的分类标签列表
        featList = [example[i] for example in dataSet]  # create a list of all the examples of this feature
        uniqueVals = set(featList)          # get a set of unique values
        newEntropy = 0.0
        # (以下五行)计算每种划分方式的信息熵
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        # tableVocabulary[i] = newEntropy
        infoGain = baseEntropy - newEntropy  # calculate the info gain; ie reduction in entropy
        if (infoGain > bestInfoGain):        # compare this to the best gain so far
            # 计算最好的信息增益
            bestInfoGain = infoGain           # if better than current best, set to best
            bestFeature = i
    # return tableVocabulary                  # finding the min and min is the best choice
    return bestFeature

# table = chooseBestFeatureToSplit(myDat)
# min = 1.7976931348623157e+308
# nick = 0
# for key in table:
#    print(str(key) + "->" + str(table[key]))
#    if table[key] <= min:
#        nick = key
#       min = table[key]
# print("\n")

# 多数表决决定叶子节点的分类。
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.key():
            classCount[vote] = 0;
        classCount[vote] += 1
        # operator 操作键值排序字典
        sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]

# 创建树。
def createTree(dataSet, labels):  
    classList = [example[-1] for example in dataSet] 
    # (以下两行)类别完全相同则停止继续划分，返回类标签-叶子节点
    if classList.count(classList[0]) == len(classList):     
        return classList[0]  
    # (以下两行)遍历完所有特征值时返回出现次数最多的
    if len(dataSet[0]) == 1:  
        return majorityCnt(classList) 
    bestFeat = chooseBestFeatureToSplit(dataSet)  
    bestFeatLabel = labels[bestFeat]  
    myTree = {bestFeatLabel:{}}  
    # 得到列表包含的所有属性值
    del(labels[bestFeat])  
    featValues = [example[bestFeat] for example in dataSet] 
    uniqueVals = set(featValues)  
    for value in uniqueVals:  
        subLabels = labels[:]  
        # 递归调用 createTree() 函数，并且将返回的 tree 插入到 myTree 字典中，  
        # 利用最好的特征划分的子集作为新的 dataSet 传入到 createTree() 函数中。  
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)  
    return myTree  

myTree = createTree(myDat, labels)
print(myTree)
print("\n")
