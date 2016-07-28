#coding:utf-8
"""
    Created on 2016/7/1 0001
    @Author:   HuShiwei
"""
'''
slppp6.intermind.net - - [01/Aug/1995:00:00:13 -0400] "GET /history/apollo/images/apollo-logo.gif HTTP/1.0" 200 3047
'''
import re
str="01/Aug/1995:00:00:14 -0400"
print str[7:11]
ma={'ss':3}
print ma['ss']

log='slppp6.intermind.net - - [01/Aug/1995:00:00:13 -0400] "GET /history/apollo/images/apollo-logo.gif HTTP/1.0" 200 3047'


regex='^(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] "(\S+) (\S+)\s*(\S*)" (\d{3}) (\S+)'

tu=(1,3)
print tu[0]

from pyspark.sql import Row

row=Row(
    tablename="sparksql",
    username='root',
    password="123456"
)

print row.username


import os
spark_home=os.environ.get("SPARK_HOME",None)
print spark_home

m=re.search('(?<=abc)def','abcdef')
print m.group(0)

import datetime
print 'This was last run on: {0}'.format(datetime.datetime.now())