#coding=utf-8
'''
该算法为最近邻算法，是无需训练过程的分类算法
输入数据：
训练集数据：第一行为属性名称，第一行的最后一项是标签名称
之后每一行是数值型的数据
最后一列为所属的类别标签
测试集数据：第一行属性名，其他行为数值型数据。没有标签
'''
from numpy import *
import operator
from os import listdir

def readTrainData(filename):
    fr = open(filename)
    attributeList=fr.readline().strip().split('\t')
    numberOfAttributes = len(attributeList)-1
    numberOfLines = len(fr.readlines())         #get the number of lines in the file
    #print "numberOfLines is :%d"%numberOfLines
    #print "numberOf attributs is:%d"%numberOfAttributes
    fr.close()
    returnMat = zeros((numberOfLines,numberOfAttributes))        #prepare matrix to return
    classLabelVector = []                       #prepare labels return
    fr = open(filename)
    index = 0
    fr.readline()
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:numberOfAttributes]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    fr.close()
    return returnMat,classLabelVector,attributeList

def readTestData(filename):
    fr = open(filename)
    attributeList=fr.readline().strip().split('\t')
    numberOfAttributes = len(attributeList)
    numberOfLines = len(fr.readlines())         #get the number of lines in the file
    #print "numberOfLines is :%d"%numberOfLines
    #print "numberOf attributs is:%d"%numberOfAttributes
    fr.close()
    returnMat = zeros((numberOfLines,numberOfAttributes))        #prepare matrix to return
    fr = open(filename)
    index = 0
    fr.readline()
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[:]
        index += 1
    fr.close()
    return returnMat,attributeList


def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m,1))
    normDataSet = normDataSet/tile(ranges, (m,1))   #element wise divide
    return normDataSet, ranges, minVals

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount


#trainFileName:训练集文件名
#testFileName:测试集文件名称
#k: knn算法中的参数k
def knnClassification(trainFileName,testFileName,k=3):
    
    dataMat1,dataLabel1,dataAttrbuteName1 = readTrainData(trainFileName)       #load data setfrom file
    dataMat2,dataAttrbuteName2 = readTestData(testFileName)
    f=open('result.txt','w')
    for i in range(len(dataMat2)):
        classifierResult = classify0(dataMat2[i,:],dataMat1,dataLabel1,k)
        print "%d\t"%i,dataMat2[i].tolist(),"\t%d\n"%classifierResult[0][0]
        currentList=str(dataMat2[i].tolist())
        currentList=currentList.replace("[","")
        currentList=currentList.replace("]","")
        currentList=currentList.replace("'","")
        currentList=currentList.replace(",","\t")
        #currentList=currentList+"%d\n"%classifierResult[0][0]
        #print type(classifierResult[0][0])
        f.write(currentList)
        f.write("\t%d\n"%classifierResult[0][0])
    f.close()


if __name__=="__main__":
    knnClassification("trainSet.txt","testSet.txt",3)





