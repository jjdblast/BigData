#coding=utf-8

'''
区域经济外向度竞争力指数 
param1: 进出口总额
param2: 进出口增长率
param3: 出口总额
param4: 出口增长率
param5: 实际FDI 
param6: 实际FDI增长率
param7: 对外经济合作完成营业额
param8: 年末在外劳务人数 
param9: 外资企业进出口占进出口总额比重 
param10: 外贸依存度
'''

def getIndex(param1,param2,param3,param4,param5,param6,param7,param8,param9,param10):
	result=0.1*param1+0.096*param2+0.134*param3+0.101*param4+0.117*param5+0.094*param6+0.07*param7+0.064*param8+0.075*param9+0.153*param10
	return result
