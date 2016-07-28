#coding=utf-8
'''
该算法为基于距离的聚类算法
输入数据：第一行为属性名称
其他行均为数值型数据
确定k值后会产生k个聚类中心，并对数据集中的每一条数据分配它的聚类中心。
聚类的结果将会保存到result.txt文件中
'''
from numpy import *
import math
def loadDataSet(fileName):      #general function to parse tab -delimited floats
    dataMat = []                #assume last column is target value
    fr = open(fileName)
    label=fr.readline().strip().split('\t')
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float,curLine) #map all elements to float()
        dataMat.append(fltLine)
    return dataMat,label

def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2))) #la.norm(vecA-vecB)

def randCent(dataSet, k):
    n = shape(dataSet)[1]
    centroids = mat(zeros((k,n)))#create centroid mat
    for j in range(n):#create random cluster centers, within bounds of each dimension
        
        minJ = min(dataSet[:,j])
        rangeJ = float(max(dataSet[:,j]) - minJ)
        centroids[:,j] = mat(minJ + rangeJ * random.rand(k,1))
    return centroids


def kMeans(fileName, k=3, distMeas=distEclud, createCent=randCent):
    dataSet,label=loadDataSet(fileName)
    dataSet=array(dataSet)
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m,2)))#create mat to assign data points 
                                      #to a centroid, also holds SE of each point
    centroids = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):#for each data point assign it to the closest centroid
            minDist = inf; minIndex = -1
            for j in range(k):
                distJI = distMeas(centroids[j,:],dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI; minIndex = j
            if clusterAssment[i,0] != minIndex: clusterChanged = True
            clusterAssment[i,:] = minIndex,minDist**2
        #print centroids
        for cent in range(k):#recalculate centroids
            ptsInClust = dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]#get all the point in this cluster
            centroids[cent,:] = mean(ptsInClust, axis=0) #assign centroid to mean

    print "the %d cluster centers are:"%k
    for i in range(k):
        print "the %d center is:"%i,centroids[i]
    print "number\t",label,"\tcluster"
    f=open('result.txt','w')
    for i in range(m):
        print "%d\t"%i,dataSet[i],"\t%d"%int(clusterAssment[i,0])
        currentList=str(dataSet[i])
        currentList=currentList.replace("[","")
        currentList=currentList.replace("]","")
        currentList=currentList.replace("'","")
        currentList=currentList.replace(",","\t")
        f.write(currentList)
        f.write("\t%d\n"%clusterAssment[i,0])
    f.close()
    return centroids, clusterAssment

if __name__=="__main__":
    center,cluster=kMeans("testSet.txt",3)

