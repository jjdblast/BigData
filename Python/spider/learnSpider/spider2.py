# coding:utf-8
'''
    Created on 2016/6/18 0018 
    @Author:   HuShiwei
'''

import re

# compile方法里面放正则表达式
pattern = re.compile(r'hello')

result1 = re.match(pattern, 'hello')
result2 = re.match(pattern, 'helloO CQC')
result3 = re.match(pattern, 'helo CQC')
result4 = re.match(pattern, 'hello CQC')

if result1:
    print result1.group()
else:
    print '1error'

if result2:
    print result2.group()
else:
    print '2error'

if result3:
    print result3.group()
else:
    print '3error'

if 4:
    print result4.group()
else:
    print '4error'
