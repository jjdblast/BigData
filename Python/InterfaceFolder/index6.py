#coding=utf-8

'''
区域政府作用竞争力指数 
param1: 区域政府发展经济竞争力指数
param2: 区域政府调规经济竞争力指数
param3: 区域政府保障经济竞争力指数
'''

def getIndex(param1,param2,param3):
	result=0.366*param1+0.317*param2+0.317*param3
	return result
