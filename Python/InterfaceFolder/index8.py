#coding=utf-8

'''
区域财政金融竞争力指数
param1: 区域财政竞争力指数 
param2: 区域金融竞争力指数
'''

def getIndex(param1,param2):
	result=0.55*param1+0.45*param2
	return result
