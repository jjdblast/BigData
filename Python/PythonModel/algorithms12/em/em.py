#coding:utf-8
'''
em最大期望算法是一种从不完全数据或有数据丢失的数据集中求解概率模型参数的最大似然估计方法。
这里模拟k=2个正态分布的均值估计
输入数据可通过generateData.py产生,详细参数见generateData.py内注释
'''
import math
import copy
import numpy as np

isdebug = False

def loadDataSet(fileName):
    f=open(fileName)
    firstline=f.readline().strip().split("\t")
    sigma=int(firstline[0])
    k=int(firstline[1])
    n=int(firstline[2])
    x=[]
    for line in f.readlines():
        x.extend([float(line)])
    return np.array([x]),sigma,k,n


# EM算法：步骤1，计算E[zij]
def e_step(Sigma,k,N):
    global Expectations
    global Mu
    global X
    for i in xrange(0,N):
        Denom = 0
        for j in xrange(0,k):
            Denom += math.exp((-1/(2*(float(Sigma**2))))*(float(X[0,i]-Mu[j]))**2)
        for j in xrange(0,k):
            Numer = math.exp((-1/(2*(float(Sigma**2))))*(float(X[0,i]-Mu[j]))**2)
            Expectations[i,j] = Numer / Denom
    if isdebug:
        print "***********"
        print u"隐藏变量E（Z）："
        print Expectations


# EM算法：步骤2，求最大化E[zij]的参数Mu
def m_step(k,N):
    global Expectations
    global X
    for j in xrange(0,k):
        Numer = 0
        Denom = 0
        for i in xrange(0,N):
            Numer += Expectations[i,j]*X[0,i]
            Denom +=Expectations[i,j]
        Mu[j] = Numer / Denom


'''
trainFileName:服从高斯分布的数据文件
iter_num:最大迭代次数
Epsilon:停止条件，当两次迭代误差小于精度Epsilon时停止迭代
'''
def run(trainFileName,iter_num,Epsilon):
    global X
    global Mu
    global Expectations
    X,Sigma,k,N=loadDataSet(trainFileName)
    Mu = np.random.random(2)
    Expectations = np.zeros((N,k))
    print X
    print u"初始<u1,u2>:", Mu
    f=open('result.txt','w')
    f.write('interation_times\t[mu1\tmu2]\n')
    for i in range(iter_num):
        Old_Mu = copy.deepcopy(Mu)
        e_step(Sigma,k,N)
        m_step(k,N)
        f.write('%d '%i)
        f.write(str(Mu))
        f.write('\n')
        print i,Mu
        if sum(abs(Mu-Old_Mu)) < Epsilon:
            break
    f.close()
if __name__ == '__main__':
    run('trainSet.txt',1000,0.0001)