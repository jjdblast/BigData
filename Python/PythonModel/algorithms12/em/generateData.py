#coding=utf-8
'''
该代码用于生成高斯分布的训练文件,这里的高斯分布具有相同的均方差sigma
'''
import numpy as np

'''
sigma:方差
Mu1:第一个高斯分布的均值
Mu2:第二个高斯分布的均值
k:模拟k个高斯分布的均值估计，这里k默认为2
N:生成训练样本的数量
'''
def ini_data(Sigma,Mu1,Mu2,k=2,N=1000):
    global X
    X = np.zeros((1,N))
    for i in xrange(0,N):
        if np.random.random(1) > 0.5:
            X[0,i] = np.random.normal()*Sigma + Mu1
        else:
            X[0,i] = np.random.normal()*Sigma + Mu2
    input=str(X)
    input=input.replace('[','')
    input=input.replace(']','')
    f=open('trainSet.txt','w')
    f.write('%d\t%d\t%d\n'%(Sigma,k,N))
    for i in range(len(X[0])):
        f.write('%f\n'%X[0,i])
    f.close()

if __name__=="__main__":
    ini_data(6,40,20,2,1000)