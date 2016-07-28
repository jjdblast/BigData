#coding=utf-8

'''
区域经济实力竞争力指数 
param1: 地区生产总值
param2: 地区生产总值增长率
param3: 人均地区生产总值
param4: 财政总收入
param5: 财政总收入增长率
param6: 人均财政总收入
param7: 固定资产投资额
param8: 固定资产投资额增长率
param9: 人均固定资产投资额
param10: 全社会消费品零售总额
param11: 全社会消费品零售总额增长率 
param12: 人均全社会消费品零售总额
'''

def getIndex(param1,param2,param3,param4,param5,param6,param7,param8,param9,param10,param11,param12):
	result=0.105*param1+0.095*param2+0.098*param3+0.09*param4+0.088*param5+0.088*param6+0.094*param7+0.08*param8+0.077*param9+0.08*param10+0.077*param11+0.08*param12
	return result
