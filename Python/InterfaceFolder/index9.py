#coding=utf-8

'''
区域财政竞争力指数 
param1: 地方财政收入
param2: 税性收入占地方财政收入比重
param3: 财政支出
param4: 地方财政收入占GDP 
param5: 税性收入占GDP
param6: 财政支出占GDP 
param7: 人均地方财政收入
param8: 人均税收收入
param9: 人均财政支出 
param10: 地方财政收入年递增
param11: 税性收入年递增 
param12: 财政支出年递增
'''

def getIndex(param1,param2,param3,param4,param5,param6,param7,param8,param9,param10,param11,param12):
	result=0.08*param1+0.079*param2+0.08*param3+0.103*param4+0.09*param5+0.084*param6+0.084*param7+0.084*param8+0.079*param9+0.08*param10+0.08*param11+0.078*param12
	return result
