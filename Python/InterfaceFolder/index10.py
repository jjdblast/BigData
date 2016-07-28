#coding=utf-8

'''
区域人力资源竞争力指数 
param1: 人口自然增长率
param2: 十五到六四岁人口比例 
param3: 文盲率
param4: 大专以上教育程度人口比例
param5: 平均受教育程度
param6: 人口健康素质预期寿命 
param7: 就业总人数占十五至六四岁人口比重
'''

def getIndex(param1,param2,param3,param4,param5,param6,param7):
	result=0.156*param1+0.137*param2+0.124*param3+0.16*param4+0.135*param5+0.144*param6+0.144*param7
	return result
