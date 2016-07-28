#coding:utf-8
'''
Created on 2016/6/5 0005

@author: HuShiwei
'''

import os
import os.path
import commands
rootdir="E:/bigdataData/ml-100k"

for parent,dirname,filename in os.walk(rootdir):
    for dirname in dirname:
        print "parent is: "+parent
        print "dirname is: "+dirname

    print "============================="

    for filename in filename:
        # print "parent is: "+parent
        print "filename is: "+filename
        # print "the full name of the file is: "+os.path.join(parent,filename)

