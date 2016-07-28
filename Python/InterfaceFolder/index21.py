#coding=utf-8

'''
区域教育竞争力指数 
param1: 教育经费占GDP比重
param2: 人均教育经费 
param3: 人均文化教育支出占个人消费支出比重
param4: 万人中小学学校数 
param5: 万人中小学专任教师数
param6: 万人中高中和高等学校在校学生数
param7: 万人高等学校数 
param8: 万人高校专任教师数
'''

def getIndex(param1,param2,param3,param4,param5,param6,param7,param8):
	result=0.186*param1+0.177*param2+0.117*param3+0.102*param4+0.098*param5+0.112*param6+0.106*param7+0.102*param8
	return result
