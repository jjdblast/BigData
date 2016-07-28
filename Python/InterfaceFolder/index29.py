#coding=utf-8

'''
区域资源竞争力指数 
param1: 人均国土面积
param2: 人均海域面积
param3: 人均年水资源总量
param4: 耕地面积
param5: 人均耕地面积
param6: 主要能源矿产基础储量
param7: 人均主要能源矿产基础储量 
param8: 人均森林储积量
param9: 资源综合利用指数
'''

def getIndex(param1,param2,param3,param4,param5,param6,param7,param8,param9):
	result=0.108*param1+0.106*param2+0.097*param3+0.103*param4+0.103*param5+0.103*param6+0.097*param7+0.139*param8+0.144*param9
	return result
