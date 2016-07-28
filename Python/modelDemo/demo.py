# coding:utf-8
'''
Created on 2016/6/5 0005

@author: admin
'''

import sys
# sys.path.append("E:/InterfaceFolder")

# from InterfaceFolder import *

if __name__ == '__main__':
    function = "Interface"
    for i in range(5):
        eval("%s.my_callback" % function)(i)
