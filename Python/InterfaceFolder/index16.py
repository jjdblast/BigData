#coding=utf-8

'''
区域工业竞争力指数 
param1: 工业增加值
param2: 工业增加值增长率
param3: 人均工业增加值 
param4: 工业资产总额
param5: 工业资产总额增长率
param6: 工业资产总贡献率
param7: 规模以上工业增加值占工业增加值比重
param8: 工业全员劳动生产率
param9: 工业成本费用利润率 
param10: 工业产品销售率
'''

def getIndex(param1,param2,param3,param4,param5,param6,param7,param8,param9,param10):
	result=0.113*param1+0.108*param2+0.103*param3+0.108*param4+0.093*param5+0.093*param6+0.096*param7+0.099*param8+0.093*param9+0.094*param10
	return result
