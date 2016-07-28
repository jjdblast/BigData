#coding=utf-8

'''
区域政府发展经济竞争力指数 
param1: 财政支出用于基本建设投资比重
param2: 财政支出对GDP增长的拉动GDP除财政支出 
param3: 政府公务员对经济的贡献公务员人均GDP
param4: 政府消费对民间消费的拉动居民消费除政府消费
param5: 财政投资对社会投资的拉动全社会固定资产除财政对固定资产的投资
'''

def getIndex(param1,param2,param3,param4,param5):
	result=0.202*param1+0.201*param2+0.196*param3+0.197*param4+0.204*param5
	return result
