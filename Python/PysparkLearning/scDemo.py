# coding:utf-8
'''
    Created on 2016/7/5 0005 
    @Author:   HuShiwei
'''

from pyspark import SparkConf,SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName("pyspark").setMaster("local[*]")
    sc=SparkContext(conf=conf)

    data=xrange(1,10001)
    xrangeRDD=sc.parallelize(data,8)
    help(sc.parallelize)