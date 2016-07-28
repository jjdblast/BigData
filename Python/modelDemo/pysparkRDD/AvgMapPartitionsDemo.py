# coding:utf-8
'''
    Created on 2016/6/22 0022 
    @Author:   HuShiwei
'''

# 使用mappartions求所有数的平均数
'''mappartitions接的参数是一个iterator,输出的参数也得是一个iterator'''
import sys

from pyspark import SparkContext


def partionCtr(nums):
    sumCount = [0, 0]
    for i in nums:
        sumCount[0] += i
        sumCount[1] += 1
    return [sumCount]

def combineCtrs(c1,c2):
    return (c1[0]+c2[0],c1[1]+c2[1])

def basicAvg(num):
    sumCount=nums.mapPartitions(partionCtr).reduce(combineCtrs)
    return sumCount[0]/sumCount[1]

if __name__ == '__main__':
    cluster = "local"
    if len(sys.argv) == 2:
        cluster = sys.argv[1]
    sc = SparkContext(cluster, "mappartions")
    nums = sc.parallelize([1, 2, 3, 4])
    avg=basicAvg(nums)
    print avg

    result=nums.sum()
    count=nums.count()
    avg1=result/count
    print avg1
    sc.stop()
