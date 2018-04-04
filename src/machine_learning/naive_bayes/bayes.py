'''
Created on 2018年4月4日
@author: WuPing
'''

from numpy import *
import sys

# 从文本中构建向量
def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
             ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
             ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
             ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
             ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
             ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]    # 分别表示标签, 1 代表侮辱性文字, 0 代表正常言论
    return postingList, classVec     # 返回输入数据和标签向量

def createVocabList(dataSet):
    vocabSet = set([])     # 创建一个空集
    for document in dataSet:
        vocabSet = vocabSet | set(document)  # 创建两个集合的并集
    return list(vocabSet)  # 输出不重复的元素

def setOfWords2Vec(vocabList, inputSet):   # 判断了一个词是否出现在一个文档当中
    returnVec = [0]*len(vocabList)  # 创建一个其中所含元素都为 0 的向量
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else: print("the word: %s is not in my Vocabulary!" % word)
    return returnVec   # 输入中的元素在词汇表时，词汇表相应位置为 1，否则为 0

dataSet, classes = loadDataSet()
print(dataSet)
vocabList = createVocabList(dataSet)
print(vocabList)
setWordsVec = setOfWords2Vec(vocabList, dataSet[0])
print(setWordsVec)
