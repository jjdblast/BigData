#coding=utf-8
'''
该算法为标称型数据的决策树算法
数据要求：输入数据第一行为各属性名称
之后每一行为具体数据，数据类型为标称型
最后一列为分类标签
分为训练集和测试集
输出结果保存到result.txt文件中，倒数第二列是真是类别，最后一列是分类结果。
'''
from math import log
import operator

def readData(filename):
    fr = open(filename)
    firstLine=fr.readline().strip().split('\t')
    labels=firstLine[:-1]        #get the number of lines in the file
    fr.close()
    fr = open(filename)
    fr.readline()
    dataSet=[]
    for line in fr.readlines():
        currentline = line.strip().split('\t')
        dataSet.append(currentline)
    fr.close()
    return dataSet,labels


def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet: #the the number of unique elements and their occurance
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys(): labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob,2) #log base 2
    return shannonEnt
    
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]     #chop out axis used for splitting
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet
    
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1      #the last column is used for the labels
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0; bestFeature = -1
    for i in range(numFeatures):        #iterate over all the features
        featList = [example[i] for example in dataSet]#create a list of all the examples of this feature
        uniqueVals = set(featList)       #get a set of unique values
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)     
        infoGain = baseEntropy - newEntropy     #calculate the info gain; ie reduction in entropy
        if (infoGain > bestInfoGain):       #compare this to the best gain so far
            bestInfoGain = infoGain         #if better than current best, set to best
            bestFeature = i
    return bestFeature                      #returns an integer

def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def createTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList): 
        return classList[0]#stop splitting when all of the classes are equal
    if len(dataSet[0]) == 1: #stop splitting when there are no more features in dataSet
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]       #copy all of labels, so trees don't mess up existing labels
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value),subLabels)
    return myTree                            
    
def classify(inputTree,featLabels,testVec):
    firstStr = inputTree.keys()[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    key = testVec[featIndex]
    valueOfFeat = secondDict[key]
    if isinstance(valueOfFeat, dict): 
        classLabel = classify(valueOfFeat, featLabels, testVec)
    else: classLabel = valueOfFeat
    return classLabel

def explaination(treeDict,labels,parent,level):
    for key in treeDict:
        if key in labels:
            print "%d层:以属性%s为节点进行判断"%(level+1,key)
            if type(treeDict[key]).__name__=='dict':
                explaination(treeDict[key],labels,key,level+1)
            else:
                pass
        else:
            if parent is "null":
                print "%d层:以属性%s进行判断"%(level,key)
            else:
                print "%d层:如果%s为%s"%(level,parent,key)
            if type(treeDict[key]).__name__=='dict':
                if parent!="null":
                    print "进行进一步判断"
                explaination(treeDict[key],labels,key,level)
            else:
                print "最终结果为%s"%treeDict[key]

def ID3(trainFile,testFile):
    trainSet, trainLabels=readData("trainSet.txt")
    testSet, testLabels=readData("testSet.txt")
    treeResult= createTree(trainSet,trainLabels)
    f=open("result.txt","w")
    for i in range(len(testSet)):
        classLabel=classify(treeResult,testLabels,testSet[i])
        currentList=str(testSet[i])
        currentList=currentList.replace("[","")
        currentList=currentList.replace("]","")
        currentList=currentList.replace(",","\t")
        currentList=currentList.replace("'","")
        f.write(currentList)
        f.write("\t")
        f.write(str(classLabel))
        f.write("\n")
    f.close()


if __name__=="__main__":
    ID3("trainSet.txt","testSet.txt")
    #print "构建的决策树描述如下："
    #explaination(treeResult,labels,"null",1)

