#coding=utf-8

'''
区域基础设施竞争力指数 
param1: 人均铁路长度
param2: 人均公路长度
param3: 人均内河航道里程
param4: 全社会旅客周转量
param5: 全社会货物周转量
param6: 人均邮电业务总量
param7: 万户移动电话数 
param8: 万人上网用户数
param9: 人均耗电量
'''

def getIndex(param1,param2,param3,param4,param5,param6,param7,param8,param9):
	result=0.11*param1+0.12*param2+0.099*param3+0.129*param4+0.129*param5+0.102*param6+0.101*param7+0.095*param8+0.115*param9
	return result
