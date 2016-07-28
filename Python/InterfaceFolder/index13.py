#coding=utf-8

'''
区域城市化进程竞争力指数 
param1: 城镇人口比重
param2: 城镇居民人均可支配收入
param3: 城市平均建成区面积量
param4: 人均拥有道路面积
param5: 人均日生活用水量
param6: 人均居住面积
param7: 人均城市园林绿化面积
'''

def getIndex(param1,param2,param3,param4,param5,param6,param7):
	result=0.225*param1+0.175*param2+0.136*param3+0.124*param4+0.114*param5+0.12*param6+0.106*param7
	return result
