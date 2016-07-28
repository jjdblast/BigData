#coding=utf-8

'''
区域农业竞争力指数 
param1: 农业增加值
param2: 农业增加值增长率
param3: 人均农业增加值
param4: 乡镇企业增加值
param5: 农民人均纯收入
param6: 农民人均纯收入增长率
param7: 农产品出口额占农林渔牧业总产值比重
param8: 人均主要农产品产量
param9: 农业劳动生产率 
param10: 农村人均固定资产原值
param11: 农村人均用电量
param12: 支农资金比重
'''

def getIndex(param1,param2,param3,param4,param5,param6,param7,param8,param9,param10,param11,param12):
	result=0.105*param1+0.086*param2+0.048*param3+0.048*param4+0.105*param5+0.089*param6+0.086*param7+0.086*param8+0.102*param9+0.102*param10+0.08*param11+0.063*param12
	return result
