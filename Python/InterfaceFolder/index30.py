#coding=utf-8

'''
区域软环境竞争力指数 
param1: 外资企业数增长率
param2: 个体私营企业数增长率
param3: 每万人上表注册件数
param4: 查处上表侵权假冒案件 
param5: 每十万人火灾发生数
param6: 每十万人交通事故发生数
param7: 罚没收入除财政收入
'''

def getIndex(param1,param2,param3,param4,param5,param6,param7):
	result=0.173*param1+0.173*param2+0.127*param3+0.123*param4+0.111*param5+0.114*param6+0.177*param7
	return result
