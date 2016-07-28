#coding=utf-8
'''
    输入数据dict中每个key对应的意思是：
    1：工业增加值
    2：工业增加值增长率
    3：人均工业增加值
    4：工业资产总额
    5：工业资产总额增长率
    6：工业资产总贡献率
    7：规模以上工业增加值占工业增加值比重
    8：工业全员劳动生产率
    9：工业成本费用利用率
    10：工业产品销售率
'''
def readData(filename):
    file=open(filename)
    dict={}
    for line in file.readlines():
        currentLine=line.strip().split(":")
        dict[float(currentLine[0])]=float(currentLine[1])
    file.close()
    return dict

def calculation(dict):
    result=0.113*dict[1]+0.108*dict[2]+0.103*dict[3]+0.108*dict[4]+0.093*dict[5]+0.093*dict[6]+0.096*dict[7]+0.099*dict[8]+0.093*dict[9]+0.094*dict[10]
    return result


if __name__=="__main__":
    dict=readData("C:\jusfoun\dataSet.txt")
    result=calculation(dict)
    print "区域工业竞争力指数是:%f\n"%result
