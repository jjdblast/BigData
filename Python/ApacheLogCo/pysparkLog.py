#coding:utf-8
'''
    Created on 2016/7/1 0001 
    @Author:   HuShiwei
'''

import sys
import os
from test_helper import Test

baseDir=os.path.join('databricks-datasets')
inputPath=os.path.join('cs1000','lab2','data-001','apache.access.log.PROGECT')
logFile=os.path.join(baseDir,inputPath)

def parseLogs():
    '''Read and parse log file'''
    # parsed_logs=(sc.te)