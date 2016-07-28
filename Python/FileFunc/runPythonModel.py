# coding:utf-8
'''
Created on 2016/6/5 0005

@author: hushiwei
'''

import sys
from pyspark import SparkConf, SparkContext
# PythonModelFodel="D:/Coding/PythonWorkStation/InterfaceFolder"
# PythonModelFodel="E:\\InterfaceFolder"
# sys.path.append(PythonModelFodel)


# 需要模型的名字:Interface，模型的方法:my_callback
# 然后用eval去执行这个方法
# i是方法需要的参数
#


if __name__ == '__main__':
    function = "index2"

    path = "hdfs://ubt202:8020/xym/py/"

    conf = SparkConf().setAppName("python model").setMaster("local[*]")
    sc = SparkContext(conf=conf)


    def mapMethod(x,function):
        a=x.split(" ")
        exec("import %s" % function)
        value= eval("%s.getIndex" % function)(a)
        return value


    rdd=sc.textFile(path)
    result=rdd.map(lambda x:mapMethod(x,function))
    # print result.collect()
    print result.take(10)





