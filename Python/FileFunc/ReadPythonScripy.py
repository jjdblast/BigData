# coding:utf-8
'''
    Created on 2016/6/2 0002 
    @Author:   HuShiwei
'''

import os

if __name__ == '__main__':
    print os.getcwd()
    print os.listdir(".")

fs=open("C:\jusfoun\example.py",'r')
context = fs.read()

print "python`s context: "
print context

"""if __name__=="__main__":
    dict=readData("dataSet.txt")
    result=calculation(dict)
    print "区域财政金融竞争力指数是:%f\n"%result
    """


os.mkdir("C:\jusfoun\python")
# if os.path.exists()
# 创建pythonModel.py空文件
f = open('C:\jusfoun\python\pythonModel.py', 'a')
f.write(context)

string="""
    dict=readData("dataSet.txt")
    result=calculation(dict)
    print "区域财政金融竞争力指数是:%f\\n"%result
"""
# f.write(string)

f.close()
