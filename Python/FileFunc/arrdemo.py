#coding:utf-8
'''
Created on 2016/6/7 0007

@author: HuShiwei
'''
if __name__ == '__main__':
    arr=[1,2,3]


    def getIndex(arr):
        # result=0.317*param1+0.317*param2+0.366*param3
        result = 1 * arr[0] + 1 * arr[1] + 1 * arr[2]
        return result

    print getIndex(arr=arr)