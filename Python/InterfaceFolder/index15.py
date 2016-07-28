#coding=utf-8

'''
区域工业化进程竞争力指数 
param1: 第二产业增加值占GDP比重
param2: 第二产业增加值增长率
param3: 第二产业从业人员占总就业人员比重
param4: 第二产业从业人员增长率
param5: 霍夫曼系数
param6: 恩格尔系数
'''

def getIndex(param1,param2,param3,param4,param5,param6):
	result=0.23*param1+0.163*param2+0.167*param3+0.162*param4+0.137*param5+0.141*param6
	return result
