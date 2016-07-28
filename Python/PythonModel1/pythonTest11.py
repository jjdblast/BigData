#coding:utf-8
'''

'''
import os
from pyspark import SparkConf, SparkContext
path ="hdfs://ubt202:8020/xym/py/"
# path = "hdfs://192.168.0.20:9000/data/file-0.log"
# path = "hdfs://giant:9000/data/file-0.log.lzo"
outpath = "/data/cmtest"
os.environ["SPARK_HOME"] = "/opt/modules/spark-1.5.1-bin-hadoop2.6"

def getIndex(param1,param2,param3,param4):
    result=0.275*param1+0.35*param2+0.275*param3+0.1*param4
    return result

def mapMethod(x):
    a =  x.split(" ")
    print a
    return getIndex(float(a[0]),float(a[1]), float(a[2]), float(a[3]))  
  

def partitionFunc(x):
    return hash(x) % 2


if __name__ == '__main__':
#     conf = SparkConf().setMaster("spark://192.168.0.20:7077").setAppName("PythonTest")
    conf = SparkConf().setMaster("spark://giant:7077").setAppName("PythonTest")
    conf = SparkConf().setAppName("PythonTest")
    sc = SparkContext(conf = conf)
    data1 = sc.textFile(path)
#     result = data1.map(lambda x: mapMethod(x))
    result = data1.map(lambda x: (x, 1)).reduceByKey(lambda x, y:(x+y))
    print "------data1 = sc.textFile(path) num of partitions = %s" % data1.getNumPartitions()
#     print result.collect()
    result = result.repartition(1)
    print "------data1 = sc.textFile(path) num of partitions = %s" % result.getNumPartitions()
    
    result = result.partitionBy(2, partitionFunc)
    print "------data1 = sc.textFile(path) num of partitions = %s" % result.getNumPartitions()
#     result = reuslt.partition()
    result.saveAsTextFile(outpath)
    