#coding=utf-8
'''
    dbscan基于密度的聚类算法：
    输入数据为二维数据，即n行2列
    输出保存在result.txt中，前两列是数据坐标，第三列是计算得出的所属聚类编号，
    如果有标有noise的则是噪声，不属于任何一类。
    
'''
def loadData(fileName):
    Data = []
    with open(fileName,'r') as f:
        for line in f.readlines():
            currentLine=line.strip().split(",")
            Data.append([float(currentLine[0]),float(currentLine[1])])
    #print Data
    return Data

class cluster:
    
    pList = []
    X = []
    Y = []
    name = ""
    
    def __init__(self,name):
        self.name = name
        self.pList = []
        self.X = []
        self.Y = []
    
    def addPoint(self,point):
        self.pList.append(point)
        self.X.append(point[0])
        self.Y.append(point[1])
    
    def getPoints(self):
        return self.pList
    
    def erase(self):
        self.pList = []
    
    def getX(self):
        return self.X
    
    def getY(self):
        return self.Y
    
    def has(self,point):
        
        if point in self.pList:
            return True
        
        return False
    
    def printPoints(self):
        print self.name+' Points:'
        print '-----------------'
        print self.pList
        print len(self.pList)
        print '-----------------'


class dbscanner:
    
    dataSet = []
    count = 0
    visited = []
    member = []
    Clusters = []
    
    def dbscan(self,D,eps,MinPts):
        self.dataSet = D
        
        #title(r'DBSCAN Algorithm', fontsize=18)
        #xlabel(r'Dim 1',fontsize=17)
        #ylabel(r'Dim 2', fontsize=17)
        
        C = -1
        Noise = cluster('Noise')
        f=open('result.txt','w')
        
        
        for point in D:
            if point not in self.visited:
                self.visited.append(point)
                NeighbourPoints = self.regionQuery(point,eps)
                
                if len(NeighbourPoints) < MinPts:
                    Noise.addPoint(point)
                else:
                    name = 'Cluster'+str(self.count);
                    C = cluster(name)
                    self.count+=1;
                    #print self.count
                    self.expandCluster(point,NeighbourPoints,C,eps,MinPts)
                    for a in C.pList:
                        f.write("%f\t%f\t%d\n"%(a[0],a[1],(self.count-1)))
                   
        if len(Noise.getPoints())!=0:
            for a in Noise.pList:
                f.write("%f\t%f\tnoise\n"%(a[0],a[1]))

        f.close()
                
            
    
    def expandCluster(self,point,NeighbourPoints,C,eps,MinPts):
        
        C.addPoint(point)
        
        for p in NeighbourPoints:
            if p not in self.visited:
                self.visited.append(p)
                np = self.regionQuery(p,eps)
                if len(np) >= MinPts:
                    for n in np:
                        if n not in NeighbourPoints:
                            NeighbourPoints.append(n)
                    
            for c in self.Clusters:
                if not c.has(p):
                    if not C.has(p):
                        C.addPoint(p)
                        
            if len(self.Clusters) == 0:
                if not C.has(p):
                    C.addPoint(p)
                        
        self.Clusters.append(C)
        #print self.Clusters

        #C.printPoints()
        
                    
                
                     
    def regionQuery(self,P,eps):
        result = []
        for d in self.dataSet:
            if (((d[0]-P[0])**2 + (d[1] - P[1])**2)**0.5)<=eps:
                result.append(d)
        return result
    
            
'''
    fileName:输入文件
    eps:邻域:是关于距离的参数，给定对象半径eps内的区域称为该对象的eps邻域
    Minp:如果给定对象eps邻域内的样本点数大于等于MinPts，则称该对象为核心对象
    '''
def test(fileName,eps=3,MinPts=2):
    data=loadData(fileName)
    dbc= dbscanner()
    dbc.dbscan(data, eps, MinPts)

if __name__=="__main__":
    test('inputFile.txt',3,2)

            
        
                
                 
            
            
            
            
        
