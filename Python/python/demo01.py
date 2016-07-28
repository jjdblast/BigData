#coding:utf-8
'''
    Created on 2016/5/30 0030 
    @Author:   HuShiwei
'''

from pyspark import SparkContext,SparkConf

if __name__ == '__main__':
    conf=SparkConf().setAppName("pyspark").setMaster("local[3]")
    sc=SparkContext(conf=conf)
    list=sc.parallelize(range(1,10))
    print list.first()
    accu=sc.accumulator(0)
    def mapMethod(x,accu):
        a=x.split(" ")
        print a
        accu.add(1)
        return getIndex(float(a[0]),float(a[1]),float(a[2]),float(a[3]))

    result=list.map(lambda (x):mapMethod(x,accu))

    result.first()
