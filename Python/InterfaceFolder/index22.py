#coding=utf-8

'''
区域服务业竞争力指数 
param1: 服务业增加值
param2: 服务业增加值增长率
param3: 人均服务业增加值
param4: 服务业从业人员数
param5: 服务业从业人员数增长率
param6: 限额以上批零企业利税率
param7: 限额以上餐饮企业利税率 
param8: 旅游外汇收入
param9: 社会服务业增加值
param10: 房地产经营总收入
'''

def getIndex(param1,param2,param3,param4,param5,param6,param7,param8,param9,param10):
	result=0.108*param1+0.107*param2+0.107*param3+0.092*param4+0.088*param5+0.097*param6+0.097*param7+0.104*param8+0.101*param9+0.099*param10
	return result
