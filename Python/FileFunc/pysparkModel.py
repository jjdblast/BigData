# coding:utf-8
'''
    Created on 2016/6/2 0002 
    @Author:   HuShiwei
'''
from pyspark import SparkConf, SparkContext


def mapMethod(line):
    currentLine = line.strip().split(":")
    dict[float(currentLine(0))] = float(currentLine[1])
    return dict


def calculation(dict):
    result = 0.55 * dict[1] + 0.45 * dict[2]
    return result


if __name__ == '__main__':
    path = "hdfs://ubt202:8020/hsw/dataSet.txt/"
    conf = SparkConf().setAppName("python model").setMaster("local[*]")
    sc = SparkContext(conf=conf)
    pyrdd = sc.textFile(path)
    result = pyrdd.map(lambda x: mapMethod(x))
    num = calculation(result)
    print num.collect()
