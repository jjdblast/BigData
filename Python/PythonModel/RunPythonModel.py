#coding:utf-8
'''
    Created on 2016/7/12 0012 
    @Author:   HuShiwei
'''
# 梯度下降法
from numpy import *
import numpy as np
import sys
from pyspark import SparkConf, SparkContext

path = "hdfs://ncp162:8020/hsw/testSet.txt"
outpath="hdfs://ncp162:8020/hsw/out11"

conf = SparkConf().setAppName("python model").setMaster("local[*]")
sc = SparkContext(conf=conf)
rdd=sc.textFile(path)

def initFunc(iterator):
    final_iterator=[]
    for line in iterator:
        lineArr = line.strip().split()
        final_iterator.append([1.0, float(lineArr[0]), float(lineArr[1]),float(lineArr[2])])
    return iter(final_iterator)

lines=rdd.mapPartitions(initFunc).collect()

# python中的list类型转成numpy中的矩阵matrix
print "把List类型数据转成numpy下的matrix类型，并打印出来"
ma=np.mat(lines)
print ma



def gradAscent(dataMatIn):
    dataMatrix =dataMatIn[:,:-1]
    labelMat = dataMatIn[:,-1]

    m,n = shape(dataMatrix)
    alpha = 0.001
    maxCycles = 500
    weights = ones((n,1))
    for k in range(maxCycles):
        h = 1.0/(1+exp(-dataMatrix*weights))
        error = (labelMat - h)
        weights = weights + alpha * dataMatrix.transpose()* error
    return weights

result=gradAscent(ma)
print result

data=sc.parallelize(result)

def func(iterator):
    for line in iterator:
        print line
data.foreachPartition(func)
data.saveAsTextFile(outpath)
sc.stop()