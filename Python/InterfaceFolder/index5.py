#coding=utf-8

'''
区域宏观经济竞争力指数
param1: 区域经济实力竞争力指数
param2: 区域经济结构竞争力指数
param3: 区域经济外向度竞争力指数
'''

def getIndex(param1,param2,param3):
	result=0.4*param1+0.3*param2+0.3*param3
	return result
