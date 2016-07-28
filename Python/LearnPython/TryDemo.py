#coding:utf-8
'''
    Created on 2016/5/31 0031 
    @Author:   HuShiwei
'''

# try:
#     print 'try...'
#     r=10/0
#     print 'result:',r
# except ZeroDivisionError,e:
#     print 'except:',e
# finally:
#     print 'finally...'
# print 'END'

def foo(s):
    return 10 /int(s)

def bar(s):
    return foo(s)*2

def main():
    bar('0')

main()