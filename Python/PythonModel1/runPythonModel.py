# coding:utf-8
'''
Created on 2016/6/5 0005

@author: hushiwei
'''

import sys
from pyspark import SparkConf, SparkContext
# PythonModelFodel="D:/Coding/PythonWorkStation/InterfaceFolder"
PythonModelFodel="E:\IDEA-WorkStation\PythonWorkStation\InterfaceFolder"
sys.path.append(PythonModelFodel)
import InterfaceFolder

# 需要模型的名字:Interface，模型的方法:my_callback
# 然后用eval去执行这个方法
# i是方法需要的参数
#


if __name__ == '__main__':

    function = "index3"


    path = "hdfs://ubt202:8020/xym/py/"
    outpath="hdfs://ubt202:8020/hsw/python/aa"

    conf = SparkConf().setAppName("python model").setMaster("local[*]")
    sc = SparkContext(conf=conf)

    '''
    区域发展环境竞争力指数
    param1: 区域基础设施竞争力指数
    param2: 区域软环境竞争力指数
    '''
    def getIndex(param1,param2,param3):
        result=0.317*param1+0.317*param2+0.366*param3
        # result=0*param1+0*param2+0*param3
        return result

    def mapMethod(x,function):
        a=x.split(" ")
        exec("import %s" % function)

        value= eval("%s.getIndex" % function)(float(a[0]),float(a[1]), float(a[2]))
        return value


    rdd=sc.textFile(path)
    result=rdd.map(lambda x:mapMethod(x,function))
    # print result.collect()
    print result.take(10)
    # result.saveAsTextFile(outpath)





