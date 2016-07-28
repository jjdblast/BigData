# coding:utf-8
'''
    Created on 2016/6/22 0022 
    @Author:   HuShiwei
'''
import sys

from pyspark import SparkContext


def basicAvg(num):
    sumCount = num.map(lambda x: (x, 1)).fold((0, 0), (lambda x, y: (x[0] + y[0], x[1] + x[1])))
    return sumCount[0] / float(sumCount[1])


if __name__ == '__main__':
    cluster = 'local'
    if len(sys.argv) == 2:
        cluster = sys.argv[1]
    sc = SparkContext(cluster, "basicAvg")
    num = sc.parallelize([1, 2, 3, 4])
    avg = basicAvg(num)
    print avg
    sc.stop()
