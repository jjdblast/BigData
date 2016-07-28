#coding=utf-8

'''
区域政府保障经济竞争力指数 
param1: 城市城镇社区服务设施数
param2: 农村社会保障网络数
param3: 医疗保险覆盖率享受医疗保险人数占职工总人数
param4: 养老保险覆盖率享受养老保险人数占职工总人数比重
param5: 失业保险覆盖率享受失业保险人数占职工总人数比重
param6: 下岗职工再就业率
param7: 城镇登记失业率
'''

def getIndex(param1,param2,param3,param4,param5,param6,param7):
	result=0.112*param1+0.123*param2+0.182*param3+0.182*param4+0.183*param5+0.118*param6+0.101*param7
	return result
