#coding=utf-8

'''
区域经济综合竞争力指数 
param1: 区域宏观经济竞争力 
param2: 区域产业经济竞争力
param3: 区域可持续发展竞争力
param4: 区域财政金融竞争力
param5: 区域知识经济竞争力
param6: 区域发展环境竞争力
param7: 区域政府作用竞争力
param8: 区域发展水平竞争力
'''

def getIndex(param1,param2,param3,param4,param5,param6,param7,param8):
	result=0.15*param1+0.125*param2+0.15*param3+0.1*param4+0.15*param5+0.1*param6+0.1*param7+0.125*param8
	return result
