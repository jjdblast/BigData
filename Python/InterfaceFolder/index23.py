#coding=utf-8

'''
区域环境竞争力指数 
param1: 森林覆盖率
param2: 工业废水排放达标率
param3: 工业废气处理率
param4: 工业固体废物综合处置率
param5: 人均治理工业污染投资额
param6: 三废”综合利用产值
param7: 人均生活“三废”排放量
param8: 污染直接经济损失
'''

def getIndex(param1,param2,param3,param4,param5,param6,param7,param8):
	result=0.185*param1+0.11*param2+0.11*param3+0.11*param4+0.1*param5+0.1*param6+0.1*param7+0.1*param8
	return result
