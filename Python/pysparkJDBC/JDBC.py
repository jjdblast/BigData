# coding:utf-8
'''
    Created on 2016/7/19 0019 
    @Author:   HuShiwei
'''

'''
执行命令 spark-submit --packages mysql:mysql-connector-java:5.1.39 JDBC.py   成了
'''


from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext

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

df = sqlContext.read.jdbc(url=jdbcUrl, table="country", properties=properties)
df.registerTempTable("table")
df.sql_ctx("select * from table")
list=df.rdd.collect()
print list

# df.write.parquet("")
