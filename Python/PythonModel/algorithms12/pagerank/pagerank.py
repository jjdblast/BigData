#coding=utf-8
'''
PageRank网页排名算法：
输入文件内容是一个n阶方阵，用逗号分隔，表示由n个网页构成的关系图，nij=1表示网页i上有到网页j的连接。
输出文件是n个网页的各自的得分
'''

import numpy as np
from scipy.sparse import csc_matrix

def loadData(fileName):
    output=[]
    f=open(fileName)
    for line in f.readlines():
        currentLine = line.strip().split(",")
        oneLine=[]
        for a in currentLine:
            oneLine.extend(map(int,a))
        output.append(oneLine)
    f.close()
    return np.array(output)



def pageRank(G, s = .85, maxerr = .001):
    """
        Computes the pagerank for each of the n states.
        Used in webpage ranking and text summarization using unweighted
        or weighted transitions respectively.
        Args
        ----------
        G: matrix representing state transitions
        Gij can be a boolean or non negative real number representing the
        transition weight from state i to j.
        Kwargs
        ----------
        s: probability of following a transition. 1-s probability of teleporting
        to another state. Defaults to 0.85
        maxerr: if the sum of pageranks between iterations is bellow this we will
        have converged. Defaults to 0.001
        """
    n = G.shape[0]
    
    # transform G into markov matrix M
    M = csc_matrix(G,dtype=np.float)
    rsums = np.array(M.sum(1))[:,0]
    ri, ci = M.nonzero()
    M.data /= rsums[ri]
    
    # bool array of sink states
    sink = rsums==0
    
    # Compute pagerank r until we converge
    ro, r = np.zeros(n), np.ones(n)
    while np.sum(np.abs(r-ro)) > maxerr:
        ro = r.copy()
        # calculate each pagerank at a time
        for i in xrange(0,n):
            # inlinks of state i
            Ii = np.array(M[:,i].todense())[:,0]
            # account for sink states
            Si = sink / float(n)
            # account for teleportation to state i
            Ti = np.ones(n) / float(n)
            
            r[i] = ro.dot( Ii*s + Si*s + Ti*(1-s) )

    # return normalized pagerank
    return r/sum(r)


def testing(fileName,s=.85,maxerr=0.001):
    G = loadData(fileName)
    rank = pageRank(G,s,maxerr)
    f=open('result.txt','w')
    f.write("web ID\tscore\n")
    for i in range(len(rank)):
        f.write('%d\t%f\n'%(i,rank[i]))
    f.close()





if __name__=='__main__':
    testing('inputFile.txt',s=.86,maxerr=0.001)