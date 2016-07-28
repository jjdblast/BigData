#coding=utf-8

'''
区域金融竞争力指数 
param1: 存款余额
param2: 人均存款余额
param3: 人均城乡储蓄存款
param4: 贷款余额
param5: 人均贷款余额
param6: 现金投入量
param7: 中长期贷款占全部贷款余额的比重 
param8: 保险费净收入
param9: 人均保险费净收入
param10: 证券市场交易额 
param11: 人均证券市场筹资额
'''

def getIndex(param1,param2,param3,param4,param5,param6,param7,param8,param9,param10,param11):
	result=0.115*param1+0.09*param2+0.088*param3+0.114*param4+0.105*param5+0.089*param6+0.1*param7+0.086*param8+0.074*param9+0.076*param10+0.063*param11
	return result
