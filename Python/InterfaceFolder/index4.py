#coding=utf-8

'''
区域可持续发展竞争力指数 
param1: 区域资源竞争力指数
param2: 区域环境竞争力指数
param3: 区域人力资源竞争力指数
'''

def getIndex(param1,param2,param3):
	result=0.325*param1+0.325*param2+0.35*param3
	return result
