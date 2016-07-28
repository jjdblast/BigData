#coding=utf-8

'''
区域科技竞争力指数
param1: 万人科技活动人员
param2: R&D占GDP比重
param3: 人均科技经费支出
param4: 高新技术产业规模以上企业增加值
'''

def getIndex(param1,param2,param3,param4):
	result=0.14*param1+0.189*param2+0.121*param3+0.123*param4
	return result
