#coding=utf-8

'''
区域政府调规经济竞争力指数 
param1: 物价调控居民消费价格指数至反向指标 
param2: 调控城乡消费差距城镇居民人均消费除农民人均消费是反向指标
param3: 统筹经济社会发展社会事业财政支出除经济建设财政支出
param4: 规范税收行政性收入除财政收入 是 反向指标 
param5: 人口控制人口出生率至反向指标
'''

def getIndex(param1,param2,param3,param4,param5):
	result=0.209*param1+0.211*param2+0.19*param3+0.2*param4+0.19*param5
	return result
