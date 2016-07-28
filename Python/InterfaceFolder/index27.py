#coding=utf-8

'''
区域经济结构竞争力指数 
param1: 产业结构优化度
param2: 所有制经济结构优化度
param3: 城乡经济结构优化度 
param4: 就业结构优化度
param5: 资本形成结构优化度
param6: 贸易结构优化度
param7: 结构趋同系数
'''

def getIndex(param1,param2,param3,param4,param5,param6,param7):
	result=0.179*param1+0.158*param2+0.187*param3+0.15*param4+0.131*param5+0.098*param6+0.097*param7
	return result
