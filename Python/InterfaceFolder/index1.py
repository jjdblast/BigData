#coding=utf-8

'''
区域产业经济竞争力指数 
param1: 区域农业竞争力指数
param2: 区域工业竞争力指数
param3: 区域服务业竞争力指数
param4: 区域企业竞争力指数
'''

def getIndex(param1,param2,param3,param4):
	result=0.275*param1+0.35*param2+0.275*param3+0.1*param4
	return result
