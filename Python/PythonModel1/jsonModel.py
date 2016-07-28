# coding:utf-8
'''
Created on 2016/6/6 0006

@author: HuShiwei
'''

import json

jsonstr = '[{"uid":"begin_9fc59872109ac694_1465178442598","level":1,"serviceType":"BEGIN","parameters":{}},{"uid":"dataJoin_9fc59872109ac694_1465178442598","level":"2.1","serviceType":"SQL_DATA_SOURCE","parameters":{"ip":"192.168.4.213","username":"root","pwd":"5Rb!!@bqC%","port":"3306","dbName":"company_no_del","tableName":"company","tableKey":"","batchSize":"","maxActive":"","minIdle":"","initialSize":"","dbType":"Mysql","dataStatus":1,"maxConn":10,"encoding":"UTF-8"}},{"uid":"modelR_9fc59872109ac694_1465178442598","level":"3","serviceType":"R_DATA_FUSION","parameters":{"scriptId":"null","scriptType":"R","scriptName":"/xym/r/ct_company_erate.r"}},{"uid":"mysql_9fc59872109ac694_1465178442598","level":4,"serviceType":"MYSQL_TARGET_SOURCE","parameters":{"ip":"192.168.16.166","port":"3306","username":"bigdata","pwd":"Jusfoun@2016$","dbName":"jusfoun_bigdata","tableName":"9fc59872109ac694_test2_1465178458069","batchsize":"500","isCreate":"1"}},{"uid":"end_9fc59872109ac694_1465178442598","level":12,"serviceType":"END","parameters":{}},{"uid":"connection_9fc59872109ac694_1465178442634","serviceType":"LINE","parameters":{"from":"begin_9fc59872109ac694_1465178442598","to":"dataJoin_9fc59872109ac694_1465178442598"}},{"uid":"connection_9fc59872109ac694_1465178442655","serviceType":"LINE","parameters":{"from":"dataJoin_9fc59872109ac694_1465178442598","to":"modelR_9fc59872109ac694_1465178442598"}},{"uid":"connection_9fc59872109ac694_1465178442662","serviceType":"LINE","parameters":{"from":"modelR_9fc59872109ac694_1465178442598","to":"mysql_9fc59872109ac694_1465178442598"}},{"uid":"connection_9fc59872109ac694_1465178442666","serviceType":"LINE","parameters":{"from":"mysql_9fc59872109ac694_1465178442598","to":"end_9fc59872109ac694_1465178442598"}},{"nodes":[{"h":40,"id":"begin_9fc59872109ac694_1465178442598","left":-88,"top":-262,"type":"begin","w":40},{"h":40,"id":"dataJoin_9fc59872109ac694_1465178442598","left":-88,"top":-162,"type":"dataJoin","w":40},{"h":40,"id":"modelR_9fc59872109ac694_1465178442598","left":-88,"top":-62,"type":"modelR","w":40},{"h":40,"id":"mysql_9fc59872109ac694_1465178442598","left":-88,"top":38,"type":"mysql","w":40},{"h":40,"id":"end_9fc59872109ac694_1465178442598","left":-88,"top":138,"type":"end","w":40}],"edges":[{"source":"begin_9fc59872109ac694_1465178442598","target":"dataJoin_9fc59872109ac694_1465178442598","data":{"label":"","id":"connection_9fc59872109ac694_1465178442634","type":"connection"}},{"source":"dataJoin_9fc59872109ac694_1465178442598","target":"modelR_9fc59872109ac694_1465178442598","data":{"label":"","id":"connection_9fc59872109ac694_1465178442655","type":"connection"}},{"source":"modelR_9fc59872109ac694_1465178442598","target":"mysql_9fc59872109ac694_1465178442598","data":{"label":"","id":"connection_9fc59872109ac694_1465178442662","type":"connection"}},{"source":"mysql_9fc59872109ac694_1465178442598","target":"end_9fc59872109ac694_1465178442598","data":{"label":"","id":"connection_9fc59872109ac694_1465178442666","type":"connection"}}],"ports":[]}]'

# print type(jsonstr)

# jsonArr=json.loads()

# jsonstr='[{"a":"A"},{"b":[{"b":"B"},{"c":"CC"}]}]'

obj=json.loads(jsonstr);

#获取c对应的值
# print obj[1].get("b")[1].get("c")
import TableInfo
# table=TableInfo()
# table.set_driverClass("rteter")
# print table.get_driverClass

for i in obj:
    if i.get("serviceType")=="R_DATA_FUSION":
        # table.set_driverClass("R_DATA_FUSION")
        print i

# print table.get_driverClass
if __name__ == '__main__':
    table=TableInfo()
    table.set_driverClass("hello world")
    print table.get_driverClass()
