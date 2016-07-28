#coding:utf-8
'''
    Created on 2016/5/30 0030 
    @Author:   HuShiwei
'''

from pyspark import SparkContext,SparkConf

if __name__ == '__main__':
    print "hello world"
    conf=SparkConf().setAppName("pyspark").setMaster("local[*]")
    sc=SparkContext(conf=conf)
    rdd=sc.parallelize(range(1,4)).map(lambda x:(x,"a"*x))
    print rdd.collect()

