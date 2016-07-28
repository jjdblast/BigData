#coding:utf-8
'''
Created on 2016/6/7 0007

@author: HuShiwei
'''
import json

class TableInfo(object):

    # def __init__(self,driverClass,dbUrl,dbName,userName,passwd,tableName):
    #     self.__driverClass=driverClass
    #     self.__dbUrl=dbUrl
    #     self.__dbName=dbName
    #     self.__userName=userName
    #     self.__passwd=passwd
    #     self.__tableName=tableName

    # driverClass
    def get_driverClass(self):
        return self.__driverClass
    def set_driverClass(self,driverClass):
        self.__driverClass=driverClass

    # dbUrl
    def get_dbUrl(self):
        return self.__dbUrl
    def set_dbUrl(self, dbUrl):
        self.__dbUrl = dbUrl

    # dbName
    def get_dbName(self):
        return self.__dbName
    def set_dbName(self, dbName):
        self.__dbName = dbName

    # userName
    def get_userName(self):
        return self.__userName
    def set_userName(self, userName):
        self.__userName = userName

    # passwd
    def get_passwd(self):
        return self.__passwd
    def set_passwd(self, passwd):
        self.__passwd = passwd

    # tableName
    def get_tableName(self):
        return self.__tableName
    def set_tableName(self, tableName):
        self.__tableName = tableName

    # createNewTable
    def get_createNewTable(self):
        return self.__createNewTable
    def set_createNewTable(self, createNewTable):
        self.__createNewTable = createNewTable

class ScriptInfo(object):

    # scriptId
    def get_scriptId(self):
        return self.__scriptId
    def set_scriptId(self,scriptId):
        self.__scriptId=scriptId

    # scriptType
    def get_scriptType(self):
        return self.__scriptType
    def set_scriptType(self, scriptType):
        self.__scriptType = scriptType

    # scriptName
    def get_scriptName(self):
        return self.__scriptName
    def set_scriptName(self, scriptName):
        self.__scriptName = scriptName

if __name__ == '__main__':


    sourceTable=TableInfo()
    destTable=TableInfo()
    scriptInfo=ScriptInfo()


    jsonstr = '[{"uid":"begin_9fc59872109ac694_1465178442598","level":1,"serviceType":"BEGIN","parameters":{}},{"uid":"dataJoin_9fc59872109ac694_1465178442598","level":"2.1","serviceType":"SQL_DATA_SOURCE","parameters":{"ip":"192.168.4.213","username":"root","pwd":"5Rb!!@bqC%","port":"3306","dbName":"company_no_del","tableName":"company","tableKey":"","batchSize":"","maxActive":"","minIdle":"","initialSize":"","dbType":"Mysql","dataStatus":1,"maxConn":10,"encoding":"UTF-8"}},{"uid":"modelR_9fc59872109ac694_1465178442598","level":"3","serviceType":"R_DATA_FUSION","parameters":{"scriptId":"null","scriptType":"R","scriptName":"/xym/r/ct_company_erate.r"}},{"uid":"mysql_9fc59872109ac694_1465178442598","level":4,"serviceType":"MYSQL_TARGET_SOURCE","parameters":{"ip":"192.168.16.166","port":"3306","username":"bigdata","pwd":"Jusfoun@2016$","dbName":"jusfoun_bigdata","tableName":"9fc59872109ac694_test2_1465178458069","batchsize":"500","isCreate":"1"}},{"uid":"end_9fc59872109ac694_1465178442598","level":12,"serviceType":"END","parameters":{}},{"uid":"connection_9fc59872109ac694_1465178442634","serviceType":"LINE","parameters":{"from":"begin_9fc59872109ac694_1465178442598","to":"dataJoin_9fc59872109ac694_1465178442598"}},{"uid":"connection_9fc59872109ac694_1465178442655","serviceType":"LINE","parameters":{"from":"dataJoin_9fc59872109ac694_1465178442598","to":"modelR_9fc59872109ac694_1465178442598"}},{"uid":"connection_9fc59872109ac694_1465178442662","serviceType":"LINE","parameters":{"from":"modelR_9fc59872109ac694_1465178442598","to":"mysql_9fc59872109ac694_1465178442598"}},{"uid":"connection_9fc59872109ac694_1465178442666","serviceType":"LINE","parameters":{"from":"mysql_9fc59872109ac694_1465178442598","to":"end_9fc59872109ac694_1465178442598"}},{"nodes":[{"h":40,"id":"begin_9fc59872109ac694_1465178442598","left":-88,"top":-262,"type":"begin","w":40},{"h":40,"id":"dataJoin_9fc59872109ac694_1465178442598","left":-88,"top":-162,"type":"dataJoin","w":40},{"h":40,"id":"modelR_9fc59872109ac694_1465178442598","left":-88,"top":-62,"type":"modelR","w":40},{"h":40,"id":"mysql_9fc59872109ac694_1465178442598","left":-88,"top":38,"type":"mysql","w":40},{"h":40,"id":"end_9fc59872109ac694_1465178442598","left":-88,"top":138,"type":"end","w":40}],"edges":[{"source":"begin_9fc59872109ac694_1465178442598","target":"dataJoin_9fc59872109ac694_1465178442598","data":{"label":"","id":"connection_9fc59872109ac694_1465178442634","type":"connection"}},{"source":"dataJoin_9fc59872109ac694_1465178442598","target":"modelR_9fc59872109ac694_1465178442598","data":{"label":"","id":"connection_9fc59872109ac694_1465178442655","type":"connection"}},{"source":"modelR_9fc59872109ac694_1465178442598","target":"mysql_9fc59872109ac694_1465178442598","data":{"label":"","id":"connection_9fc59872109ac694_1465178442662","type":"connection"}},{"source":"mysql_9fc59872109ac694_1465178442598","target":"end_9fc59872109ac694_1465178442598","data":{"label":"","id":"connection_9fc59872109ac694_1465178442666","type":"connection"}}],"ports":[]}]'
    obj = json.loads(jsonstr)
    for i in obj:
        dataSource=i.get("serviceType")
        para=i.get("parameters")
        if dataSource == "R_DATA_FUSION":
            print "R_DATA_FUSION ===> %s" %i
            scriptInfo.set_scriptId(para.get("scriptId"))
            scriptInfo.set_scriptType(para.get("scriptType"))
            scriptInfo.set_scriptName(para.get("scriptName"))
        elif dataSource=="SQL_DATA_SOURCE":
            print "SQL_DATA_SOURCE ===> %s" %i
            sourceTable.set_dbUrl(para.get("ip"))
            sourceTable.set_dbName(para.get("dbName"))
            sourceTable.set_userName(para.get("username"))
            sourceTable.set_passwd(para.get("pwd"))
            sourceTable.set_tableName(para.get("tableName"))
        elif dataSource=="MYSQL_TARGET_SOURCE":
            print "MYSQL_TARGET_SOURCE ===> %s" %i
            destTable.set_dbUrl(para.get("ip"))
            destTable.set_dbName(para.get("dbName"))
            destTable.set_userName(para.get("username"))
            destTable.set_passwd(para.get("pwd"))
            destTable.set_tableName(para.get("tableName"))
            destTable.set_createNewTable(para.get("isCreate"))


    print "=========script========"
    print scriptInfo.get_scriptId()
    print scriptInfo.get_scriptType()
    print scriptInfo.get_scriptName()

    print "========sourceTable========="
    print sourceTable.get_dbUrl()
    print sourceTable.get_dbName()
    print sourceTable.get_userName()
    print sourceTable.get_passwd()
    print sourceTable.get_tableName()

    print "=======destTable=========="
    print destTable.get_dbUrl()
    print destTable.get_dbName()
    print destTable.get_userName()
    print destTable.get_passwd()
    print destTable.get_tableName()
    print destTable.get_createNewTable()






























