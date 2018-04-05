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

# 朴素贝叶斯分类器训练函数
def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)  # 训练集总条数
    numWords = len(trainMatrix[0])   # 训练集中所有不重复单词总数
    pAbusive = sum(trainCategory) / float(numTrainDocs)  # 侮辱类的概率(侮辱类占总训练数据的比例)
    # 正常言论的类条件概率密度 p(某单词|正常言论) = p0Num / p0Denom
    p0Num = ones(numWords);   # 初始化分子为1
    # 侮辱性言论的类条件概率密度 p(某单词|侮辱性言论) = p1Num / p1Denom
    p1Num = ones(numWords)    # 初始化分子为 1
    # 初始化分母置为 2
    p0Denom = 2; p1Denom = 2
    # 遍历训练集数据
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:           # 若为侮辱类
            p1Num += trainMatrix[i]         # 统计侮辱类所有文档中的各个单词总数
            p1Denom += sum(trainMatrix[i])  # p1Denom 侮辱类总单词数
        else:                               # 若为正常类
            p0Num += trainMatrix[i]         # 统计正常类所有文档中的各个单词总数
            p0Denom += sum(trainMatrix[i])  # p0Denom 正常类总单词数
    # 数据取 log，即单个单词的 p(x1|c1) 取 log，防止下溢出
    p1Vect = log(p1Num / p1Denom)     # 词汇表中的单词在侮辱性言论文档中的类条件概率
    p0Vect = log(p0Num / p0Denom)     # 词汇表中的单词在正常性言论文档中的类条件概率
    return p0Vect, p1Vect, pAbusive

# 朴素贝叶斯分类函数。
def classifyNB(vec2Classify, p0Vect, p1Vect, pClass1):
    # 在对数空间中进行计算，属于哪一类的概率比较大就判为哪一类
    p1 = sum(vec2Classify * p1Vect) + log(pClass1)
    p0 = sum(vec2Classify * p0Vect) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0

def testingNB():
    listOPosts, listClasses = loadDataSet()      # 获得训练数据，类别标签
    myVocabList = createVocabList(listOPosts)    # 创建词汇表
    trainMat = []                                # 构建矩阵，存放训练数据
    # 遍历原始数据，转换为词向量，构成数据训练矩阵
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc)) # 数据转换后存入数据训练矩阵 trainMat 中
    p0V, p1V, pAb = trainNB0(array(trainMat), array(listClasses))  # 训练分类器
    # 测试数据1
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))   # 测试数据转为词向量
    print(testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb))  # 输出分类结果
    # 测试数据2
    testEntry = ['stupid', 'garbage']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb))
    
testingNB()
