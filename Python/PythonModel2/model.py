#coding=utf-8
'''
   list[0-6]分别代表：国代分类代码，工商处罚，环保处罚，海关处罚，税务处罚，失信记录，新注册企业数
   dict[时间段]['国代分类代码']=[0工商处罚，1环保处罚，2海关处罚，3税务处罚，4失信记录，5新注册企业数,6诉讼记录,7企业总数]
'''
def readData(filename,dict,key):
    file=open(filename)
    dict[key]={}
    for line in file.readlines():
        list=line.strip().split(",")
        dict[key][list[0]]=[float(list[1]),float(list[2]),float(list[3]),float(list[4]),float(list[5]),float(list[6]),float(list[7]),float(list[8])]



#iter表示有几个时间段的数据，包括最新的
def register(dict,iter):
    #历年的平均注册率
    registerHistroy={}
    #最新一年的注册率
    registerNew={}
    #最近一年与以往的平均值比较
    registerCmpToHistory={}
    for key in dict[1].keys():
        registerHistroy[key]=0
        if dict[1][key][-1] != 0:
            print dict[1][key][-1]
            for i in range(iter):
                #print i
                print dict[i+1][key]
                registerHistroy[key] = registerHistroy[key] + (dict[i+1][key][-2]/dict[i+1][key][-1]*1000000)
            registerHistroy[key]=registerHistroy[key]/iter
            registerNew[key]=dict[1][key][-2]/dict[1][key][-1]*1000000
            registerCmpToHistory[key]=registerNew[key]-registerHistroy[key]
        else:
            registerHistroy[key]=0
            registerNew[key]=0
            registerCmpToHistory[key]=0

    return registerNew,registerCmpToHistory,registerHistroy

def punishment(dict,iter):
    
    punishmentHistory={}
    punishmentNew={}
    punishmentCmpToHistory={}
    weight=[1000000,1000000,1000000,1000000,1000000,1000000]
    for key in dict[1].keys():
        punishmentHistory[key]=[0,0,0,0,0,0]
        punishmentNew[key]=[0,0,0,0,0,0]
        punishmentCmpToHistory[key]=[0,0,0,0,0,0]
        if dict[1][key][-1] != 0:
            for item in range(6):
                for i in range(iter):
                    punishmentHistory[key][item]=punishmentHistory[key][item]+(dict[i+1][key][item]/dict[i+1][key][-1]*weight[item])
                punishmentHistory[key][item]=punishmentHistory[key][item]/iter
                punishmentNew[key][item]=dict[1][key][item]/dict[1][key][-1]*weight[item]
                punishmentCmpToHistory[key][item]=punishmentNew[key][item]-punishmentHistory[key][item]
    return punishmentNew,punishmentCmpToHistory,punishmentHistory

def printDict(dict):
    print "#"*100
    max=float("-inf")
    min=float("inf")
    for key in dict.keys():
        print key,':',dict[key]
        if max < dict[key]:
            max=dict[key]
        if min > dict[key]:
            min=dict[key]
    print 'max:',max
    print 'min:',min
    print "#"*100

def printDict2(dict,iter=5):
    print "#"*100
    max=[float("-inf"),float("-inf"),float("-inf"),float("-inf"),float("-inf")]
    min=[float("inf"),float("inf"),float("inf"),float("inf"),float("inf")]
    for key in dict.keys():
        print key,':',dict[key]
        for i in range(iter):
            if max[i] < dict[key][i]:
                max[i]=dict[key][i]
            if min[i] > dict[key][i]:
                min[i]=dict[key][i]
    print 'max:',max
    print 'min:',min
    print "#"*100

def normalization(dict):
    normalizationDict={}
    max=float("-inf")
    min=float("inf")
    for key in dict.keys():
        if max < dict[key]:
            max=dict[key]
        if min > dict[key]:
            min=dict[key]
    if max is not min:
        
        for key in dict.keys():
            normalizationDict[key]=(dict[key]-min)/(max-min)
    else:
        print "no"
        for key in dict.keys():
            normalizationDict[key]=0
    return normalizationDict

def normalizationDict2(dict,iter=6):
    normalizationDict={}
    for key in dict.keys():
        normalizationDict[key]=[0,0,0,0,0,0]

    max=[float("-inf"),float("-inf"),float("-inf"),float("-inf"),float("-inf"),float("-inf")]
    min=[float("inf"),float("inf"),float("inf"),float("inf"),float("inf"),float("inf")]
    for key in dict.keys():
        for i in range(iter):
            if max[i] < dict[key][i]:
                max[i]=dict[key][i]
            if min[i] > dict[key][i]:
                min[i]=dict[key][i]

    for i in range(iter):
        if max[i] is not min[i]:
            for key in dict.keys():
                normalizationDict[key][i]=(dict[key][i]-min[i])/(max[i]-min[i])
        else:
            print "no"
            for key in dict.keys():
                normalizationDict[key][i]=0

    return normalizationDict


if __name__=="__main__":
    dict={}
    for i in range(6):
        filename="%d.txt"%(i+1)
        readData(filename,dict,i+1)
    #print dict[1]
    #print dict[7]
    registerNew,registerCmpToHistory,registerHistroy=register(dict,6)
    Ub=normalization(registerNew)
    Vb=normalization(registerCmpToHistory)

    punishmentNew,punishmentCmpTpHistory,punishmentHistory=punishment(dict,6)
    Ucdefg=normalizationDict2(punishmentNew)
    Vcdefg=normalizationDict2(punishmentCmpTpHistory)

    f=open('result.txt','w')
    for key in registerNew.keys():
        index=(-Ub[key]-Vb[key]+Ucdefg[key][0]+Ucdefg[key][1]+Ucdefg[key][2]+Ucdefg[key][3]+Ucdefg[key][4]+Ucdefg[key][5]+Vcdefg[key][0]+Vcdefg[key][1]+Vcdefg[key][2]+Vcdefg[key][3]+Vcdefg[key][4]+Vcdefg[key][5])/1.4
        #print "#"*50
        #print key
        #print "Ub:",Ub[key]
        #print "Vb:",Vb[key]
        #print "Ucdefg",Ucdefg[key]
        #print "Vcdefg",Vcdefg[key]
        f.write("%s,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f\n"%(key,Ub[key],Vb[key],Ucdefg[key][0],Ucdefg[key][1],Ucdefg[key][2],Ucdefg[key][3],Ucdefg[key][4],Ucdefg[key][5],Vcdefg[key][0],Vcdefg[key][1],Vcdefg[key][2],Vcdefg[key][3],Vcdefg[key][4],Vcdefg[key][5],index))
    f.close()
    #printDict(registerNew)
    #printDict(registerHistroy)
    #printDict(registerCmpToHistory)

    #printDict2(punishmentNew)
    #printDict2(punishmentHistory)
    #printDict2(punishmentCmpTpHistory)


