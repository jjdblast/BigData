#coding=utf-8

'''
区域企业竞争力指数 
param1: 规模以上工业企业数
param2: 规模以上企业平均资产
param3: 规模以上企业平均增加值
param4: 流动资金周转次数 
param5: 规模以上企业资产负债率
param6: 规模以上企业销售利税率
param7: 规模以上企业厂均所有者权益 
param8: 新产品产值率
param9: 企业技术开发经费占产品销售收入比重
'''

def getIndex(param1,param2,param3,param4,param5,param6,param7,param8,param9):
	result=0.109*param1+0.104*param2+0.111*param3+0.113*param4+0.09*param5+0.126*param6+0.09*param7+0.138*param8+0.119*param9
	return result
