#coding=utf-8
'''
贝叶斯文本二分类算法
输入数据：训练集每行为一句或多句话，最后一位用0或1表示该行文本的类别
        测试集每行为一句或多句话
输出数据：result.txt
'''


from numpy import *

def loadTrainingDataSet(fileNmae):
    f=open(fileNmae)
    dataMat=[]
    labelMat=[]
    for line in f.readlines():
        currentLine = line.strip().split(" ")
        lowerLine=[word.lower() for word in currentLine]
        dataMat.append(lowerLine[:-1])
        labelMat.extend(map(float,currentLine[-1]))
    return dataMat,labelMat

def loadTestingDataSet(fileNmae):
    f=open(fileNmae)
    dataMat=[]
    labelMat=[]
    for line in f.readlines():
        currentLine = line.strip().split(" ")
        lowerLine=[word.lower() for word in currentLine]
        dataMat.append(lowerLine[:])
    return dataMat

#创建一个带有所有单词的列表
def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)

def setOfWords2Vec(vocabList, inputSet):
    retVocabList = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            retVocabList[vocabList.index(word)] = 1
        else:
            print 'word ',word ,'not in dict'
    return retVocabList

#另一种模型
def bagOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec

def trainNB0(trainMatrix,trainCatergory):
    numTrainDoc = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCatergory)/float(numTrainDoc)
    #防止多个概率的成绩当中的一个为0
    p0Num = ones(numWords)
    p1Num = ones(numWords)
    p0Denom = 2.0
    p1Denom = 2.0
    for i in range(numTrainDoc):
        if trainCatergory[i] == 1:
            p1Num +=trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num +=trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num/p1Denom)#处于精度的考虑，否则很可能到限归零
    p0Vect = log(p0Num/p0Denom)
    return p0Vect,p1Vect,pAbusive

def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)    #element-wise mult
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0

'''
trainFileName:训练集文件
testFileName:测试集文件
type:分为set和bag两种，分别表示词集模型和词袋模型。
'''

def testingNB(trainFileName,testFileName,type='set'):
    listOPosts,listClasses = loadTrainingDataSet(trainFileName)
    myVocabList = createVocabList(listOPosts)
    trainMat=[]
    f=open("result.txt","w")
    if type=='set':
        for postinDoc in listOPosts:
            trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
        p0V,p1V,pAb = trainNB0(array(trainMat),array(listClasses))
        dataMat=loadTestingDataSet(testFileName)
        for testline in dataMat:
            thisDoc = array(setOfWords2Vec(myVocabList, testline))
            result=classifyNB(thisDoc,p0V,p1V,pAb)
            currentList=str(testline)
            currentList=currentList.replace("[","")
            currentList=currentList.replace("]","")
            currentList=currentList.replace("'","")
            currentList=currentList.replace(",","\t")
            f.write(currentList)
            f.write("\t%s\n"%str(result))
    elif type=='bag':
        for postinDoc in listOPosts:
            trainMat.append(bagOfWords2Vec(myVocabList, postinDoc))
        p0V,p1V,pAb = trainNB0(array(trainMat),array(listClasses))
        dataMat=loadTestingDataSet(testFileName)
        for testline in dataMat:
            thisDoc = array(bagOfWords2Vec(myVocabList, testline))
            result=classifyNB(thisDoc,p0V,p1V,pAb)
            currentList=str(testline)
            currentList=currentList.replace("[","")
            currentList=currentList.replace("]","")
            currentList=currentList.replace("'","")
            currentList=currentList.replace(",","\t")
            f.write(currentList)
            f.write("\t%s\n"%str(result))
    else:
        print "there is no type name %s"%type
    f.close()



if __name__ == '__main__':
    testingNB("trainSet.txt","testSet.txt",type='bag')