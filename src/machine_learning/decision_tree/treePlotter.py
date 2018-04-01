'''
Created on 2018年4月1日
@author: WuPing
'''

import matplotlib.pyplot as plt

# (以下三行)定义文本框和箭头格式
decisionNode = dict(boxstyle = 'sawtooth', fc = '0.8')
leafNode = dict(boxstyle = 'round4', fc = '0.8')
arrow_args = dict(arrowstyle = '<-')

# (以下两行)绘制带箭头的注解
def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(nodeTxt, xy = parentPt, xycoords = 'axes fraction',\
                            xytext = centerPt, textcoords = 'axes fraction',\
                            va = 'center', ha = 'center', bbox = nodeType, \
                            arrowprops = arrow_args)  

# 使用文本注解绘制树节点
def createPlot0():
    fig = plt.figure(1, facecolor = 'white')
    fig.clf()
    createPlot.ax1 = plt.subplot(111, frameon = False)
    plotNode('a decision node', (0.5, 0.1), (0.1, 0.5), decisionNode)
    plotNode('a leaf node', (0.8, 0.1), (0.3, 0.8), leafNode)
    plt.show()
    
# createPlot0()

def getNumLeafs(myTree):
    numLeafs = 0
    firstSides = list(myTree.keys())
    firstStr = firstSides[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        # (以下三行)测试节点的数据类型是否为字典
        if(type(secondDict[key]).__name__ == 'dict'):
            numLeafs += getNumLeafs(secondDict[key])
        else: numLeafs += 1
    return numLeafs

def getTreeDepth(myTree):
    maxDepth = 0
    firstSides = list(myTree.keys())
    firstStr = firstSides[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if(type(secondDict[key]).__name__ == 'dict'):
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else: thisDepth = 1
        if thisDepth > maxDepth: maxDepth = thisDepth
    return maxDepth

# 输出预先存储的树信息。
def retrieveTree(i):
    listOfTrees = [{'no surfacing': {0: 'no', 1:{'flippers':{0: 'no', 1: 'yes'}}}},\
                   {'no surfacing': {0: 'no', 1:{'flippers':\
                        {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}}]
    return listOfTrees[i]

myTree = retrieveTree(1)
print(getNumLeafs(myTree))
print(getTreeDepth(myTree))

# 绘制一棵完整的树。
# (以下四行)在父子节点间填充文本信息
def plotMidText(cntrPt, parentPt, txtString): 
    xMid = (parentPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]
    yMid = (parentPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]  
    createPlot.ax1.text(xMid, yMid, txtString, va="center", ha="center", rotation=30)  

def plotTree(myTree, parentPt, nodeTxt): # if the first key tells you what feat was split on  
    # (以下两行)计算宽和高
    numLeafs = getNumLeafs(myTree)  # this determines the x width of this tree  
    depth = getTreeDepth(myTree)  
    firstSides = list(myTree.keys())
    firstStr = firstSides[0]     # the text label for this node should be this  
    cntrPt = (plotTree.xOff + (1.0 + float(numLeafs)) / 2.0 / plotTree.totalW, plotTree.yOff)  
    # 标记子节点属性值
    plotMidText(cntrPt, parentPt, nodeTxt)  
    plotNode(firstStr, cntrPt, parentPt, decisionNode)  
    secondDict = myTree[firstStr]
    # (以下两行)减小y偏移
    plotTree.yOff = plotTree.yOff - 1.0 / plotTree.totalD  
    for key in secondDict.keys():  
        # test to see if the nodes are dictonaires, if not they are leaf nodes  
        if type(secondDict[key]).__name__ == 'dict':    
            plotTree(secondDict[key], cntrPt, str(key))    # recursion  
        else:   # it's a leaf node print the leaf node  
            plotTree.xOff = plotTree.xOff + 1.0 / plotTree.totalW  
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), cntrPt, leafNode)  
            plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))  
            plotTree.yOff = plotTree.yOff + 1.0 / plotTree.totalD  
    # if you do get a dictonary you know it's a tree, and the first element will be another dict  

def createPlot(inTree):  
    fig = plt.figure(1, facecolor='white')  
    fig.clf()  
    axprops = dict(xticks=[], yticks=[])  
    createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)    # no ticks  
    # createPlot.ax1 = plt.subplot(111, frameon=False) # ticks for demo puropses   
    plotTree.totalW = float(getNumLeafs(inTree))  
    plotTree.totalD = float(getTreeDepth(inTree))  
    plotTree.xOff = -0.5 / plotTree.totalW;
    plotTree.yOff = 1.0;  
    plotTree(inTree, (0.5, 1.0), '')  
    plt.show()  

createPlot(myTree)
