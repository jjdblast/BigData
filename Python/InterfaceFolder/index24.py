#coding=utf-8

'''
区域知识经济竞争力指数
param1: 区域科技竞争力指数
param2: 区域教育竞争力指数
'''

def getIndex(param1,param2):
	result=0.5*param1+0.5*param2
	return result
