# coding:utf-8
'''
    Created on 2016/6/20 0020 
    @Author:   HuShiwei
'''

"""
spark-submit --master yarn-client --driver-memory 4g --executor-memory 2g --executor-cores 4 --jars /usr/hdp/2.4.0.0-169/spark/lib/mysql-connector-java-5.1.38.jar /home/devel/hsw/mysql.py
成了
"""

import os

from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext

os.environ["SPARK_HOME"] = "/usr/hdp/2.4.0.0-169/spark"

conf = SparkConf().setAppName("python model").setMaster("local[*]")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)

hostname = "192.168.4.213"
dbname = 'sparkSQL'
jdbcPort = '3306'
properties = {
    "user": 'root',
    "password": '5Rb!!@bqC%',
    "driver": 'com.mysql.jdbc.Driver'
}
jdbcUrl = "jdbc:mysql://{0}:{1}/{2}".format(hostname, jdbcPort, dbname)
print jdbcUrl
# jdbc:mysql://192.168.4.213:3306/sparkSQL
df = sqlContext.read.jdbc(url=jdbcUrl, table="pythonModel", properties=properties)
textRDD = df.rdd
print textRDD.collect()
# Row(num1=u'0.184992', num2=u'8.721488', num3=u'0')
def func(iterator):
    list=[]
    for i in iterator:
        print i
    iter(list)
textRDD.mapPartitions(func)

def func1(iterator):
    for i in iterator:
        print i
textRDD.foreachPartition(func1)
print "--------------- %s" % df.select("*").take(30)
