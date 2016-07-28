#coding=utf-8

'''
区域市场化进程竞争力指数 
param1: 非公有制经济产值占全社会总产值比重
param2: 社会投资占投资总资金比重 
param3: 非国有单位从业人员占城镇从业人员比重
param4: 亿元以上商品市场成交额 
param5: 亿元以上商品市场成交额占全社会消费品零售总额比重
param6: 农产品商品化率
'''

def getIndex(param1,param2,param3,param4,param5,param6):
	result=0.212*param1+0.191*param2+0.176*param3+0.116*param4+0.112*param5+0.193*param6
	return result
