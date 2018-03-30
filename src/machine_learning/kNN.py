'''
Created on 2018年3月23日
@author: WuPing
'''

from numpy import *
import operator
from os import listdir # 函数 listdir 可以列出给定目录的文件名

# 创造数据集  
def createDataSet():  
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])  
    labels = ['A', 'A', 'B', 'B']  
    return group, labels  

# 第一个 kNN 分类器  inX-测试数据  dataSet-样本数据   labels-标签  k-邻近的 k 个样本  
def classify0(inX, dataSet, labels, k):  
    # 计算距离  
    dataSetSize = dataSet.shape[0]  
    diffMat = tile(inX, (dataSetSize,1))- dataSet  
    sqDiffMat = diffMat ** 2  
    sqDistances = sqDiffMat.sum(axis = 1)  
    distances = sqDistances ** 0.5  
    sortedDistIndicies = distances.argsort()  
    classCount = {}  
    # 选择距离最小的 k 个点  
    for i in range(k):  
        voteIlabel = labels[sortedDistIndicies[i]]  
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1  
    # 排序  
    sortedClassCount = sorted(classCount.items(), 
                              key = operator.itemgetter(1), reverse = True)  
    return sortedClassCount[0][0]  

# 处理输入格式问题，输入为文件名字符串，输出为训练样本矩阵和类标签向量 
# 将文本记录到转换 numPy 的解析程序  
def file2matrix(filename):  
    # 打开文件并得到文件行数  
    fr = open(filename)  
    arrayOlines = fr.readlines()  
    numberOfLines = len(arrayOlines)  
    # 创建返回的 numPy 矩阵  
    returnMat = zeros((numberOfLines, 3))  
    classLabelVector = []  
    index = 0  
    # 解析文件数据到列表  
    for line in arrayOlines:  
        line = line.strip()  
        listFormLine = line.split('\t')  
        returnMat[index,:] = listFormLine[0:3]  
        classLabelVector.append(int(listFormLine[-1]))  
        index += 1  
    return returnMat, classLabelVector  

# 归一化特征值   
def autoNorm(dataSet):
    minVals = dataSet.min(0)      # 每一列的最小值
    maxVals = dataSet.max(0)      # 每一列的最大值
    ranges = maxVals - minVals    # 幅度
    normDataSet = zeros(shape(dataSet))  # 创建一个一样规模的零数组
    m = dataSet.shape[0]          # 取数组的行
    normDataSet = dataSet - tile(minVals, (m,1))  # 减去最小值
    normDataSet = normDataSet / tile(ranges, (m,1))   # 特征值相除
    # 再除以幅度值，实现归一化，tile 功能是创建一定规模的指定数组
    return normDataSet, ranges, minVals

def datingClassTest():     # 分类器针对约会网站的测试代码
    hoRatio = 0.50
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt') # load data set from file
    normMat, ranges, minVals = autoNorm(datingDataMat)
    # 计算测试向量的数量，此步决定哪些数据用于分类器的测试和训练样本
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0
    # 计算错误率，并输出结果
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:], normMat[numTestVecs:m,:], datingLabels[numTestVecs:m], 3)
        print("the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]): errorCount += 1.0
    print("the total error rate is: %f" % (errorCount / float(numTestVecs)))
    print(errorCount)

datingDataMat, datingLabels = file2matrix('datingTestSet2.txt') # 读取文件数据

datingClassTest()

def classifyPerson():
    resultList = ["not at all","in small doses","in large doses"]  
    percentTats = float(input("percentage of time spent playing video games? "))  
    ffMiles = float(input("frequent flier miles earned per year? "))  
    iceCream = float(input("liters of ice cream consumed per year? "))  
    datingDataMat, datingLabels = file2matrix("datingTestSet2.txt") 
    # 需要对新来的测试集也做归一化，故需要用到 ranges 和 minVals 两个变量  
    normMat,ranges,minVals = autoNorm(datingDataMat)  
    inArr = array([ffMiles, percentTats, iceCream])  
    classifierResult = classify0((inArr - minVals) / ranges, normMat, datingLabels, 3)  
    print ("You will probably like this person: ", resultList[classifierResult - 1])

classifyPerson()

def img2vector(filename):
    imgVect = zeros((1, 1024))  
    fr = open(filename)  
    for i in range(32):  
        linestr = fr.readline()  
        for j in range(32):  
            imgVect[0, 32*i + j] = int(linestr[j])  
    return imgVect 

def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('trainingDigits')   # 获取目录内容
    m = len(trainingFileList)   # 目录中有多少文件
    trainingMat = zeros((m,1024))    # 创建一个 m 行 1024 列的训练矩阵，该矩阵的每一行存储一个图像
    # 从文件名解析出分类数字，该目录的文件按照规则命名，如文件 9_45.txt 的分类是 9，它是数字 9 的第 45 个实例
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]   
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)    # 类代码存储到变量 hwLabels 中
        trainingMat[i,:] = img2vector('trainingDigits/%s' % fileNameStr)
        # 对 testDigits 执行相似操作，但是不载入矩阵，而是使用 classify() 函数测试该目录下的每一个文件
    testFileList = listdir('testDigits')     # iterate through the test set
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]  
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print("the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr))
        if (classifierResult != classNumStr): 
            errorCount += 1.0
    print("\nthe total number of errors is: %d" % errorCount)
    print("\nthe total error rate is: %f" % (errorCount/float(mTest)))
    
handwritingClassTest()
