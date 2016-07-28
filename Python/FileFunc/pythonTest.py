#coding:utf-8
'''
Created on 2016年5月19日

@author: giant
'''
from pyspark import SparkConf, SparkContext
path = "hdfs://ubt202:8020/xym/py/"
outpath = "/data/cmtest"

def getIndex(param1,param2,param3,param4):
    result=0.275*param1+0.35*param2+0.275*param3+0.1*param4
    return result

def mapMethod(x):
    a =  x.split(" ")
    return getIndex(float(a[0]),float(a[1]), float(a[2]), float(a[3]))  
  
if __name__ == '__main__':
    conf = SparkConf().setAppName("PythonTest")
    sc = SparkContext(conf = conf)
    data = sc.textFile(path)
    print data.take(100)
    result = data.map(lambda x: mapMethod(x))
    print result.take(10)
    