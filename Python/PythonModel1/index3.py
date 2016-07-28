#coding=utf-8

'''
区域发展环境竞争力指数 
param1: 区域基础设施竞争力指数
param2: 区域软环境竞争力指数
'''


def getIndex(param1,param2,param3):
	result=0.317*param1+0.317*param2+0.366*param3
	# result=0*param1+0*param2+0*param3
	return result
