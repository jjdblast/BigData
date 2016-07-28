#coding:utf-8
'''
Created on 2016/6/5 0005

@author: HuShiwei
'''


import os
import os.path
import commands

print "********************遍历InterfaceFolder文件下的所有puthon模型脚本*****************************"
print "*                                                                                           *"
print "*                                   python 模型脚本                                          *"
print "*                                                                                           *"
print "********************然后把每个python脚本import到__init__.py文件中*****************************"

# PythonModelFodel="D:/Coding/PythonWorkStation/InterfaceFolder"
# PythonModelFodelFileInit="D:/Coding/PythonWorkStation/InterfaceFolder/__init__.py"
PythonModelFodel="E:/InterfaceFolder"
PythonModelFodelFileInit="E:/InterfaceFolder/__init__.py"

writeImport=open(PythonModelFodelFileInit, 'a')
compareImport=open(PythonModelFodelFileInit)
hadExistImport=compareImport.readlines()

goingToImport= os.listdir(PythonModelFodel)
for file in goingToImport:
    filerealname = os.path.splitext(file)
    content="import %s \n" %filerealname[0]
    if content != "import __init__ \n":
        if content not in hadExistImport:
            writeImport.write(content)
        else:
            pass


writeImport.close()
compareImport.close()


print "*********************************************************************************************"
print "*                                                                                           *"
print "*                             读取该__init__.py文件，检查效果                                *"
print "*                                                                                           *"
print "*********************************************************************************************"
# fileRead=open("E:/InterfaceFolder/__init__.py",'r')
fileRead=open(PythonModelFodelFileInit,'r')
filecontent=fileRead.read()
print "this is __init__.py content \n %s" %filecontent

fileRead.close()


print "================================="
# string=commands.getoutput("cat /home/hsw/__int__.py").split("\n")
# string.filter("import __init__")

import sys
sys.path.append(PythonModelFodel)

from InterfaceFolder import *

# 需要模型的名字:Interface，模型的方法:my_callback
# 然后用eval去执行这个方法
# i是方法需要的参数
#
if __name__ == '__main__':
    function = "Interface"

    eval("%s.my_callback" % function)(5)
    # for i in range(5):
    #     eval("%s.my_callback" % function)(i)