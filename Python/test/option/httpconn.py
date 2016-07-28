# coding=utf-8
__author__ = 'zenith'

import httplib,json
url = "http://192.168.1.162:34343/metrics"
conn = httplib.HTTPConnection("192.168.1.162","34343")
conn.request("GET",url)
response = conn.getresponse()
res= response.read()
obj=json.loads(res)

print obj.get("CHANNEL.c1").get("EventTakeSuccessCount"),obj.get("CHANNEL.c1").get("EventPutAttemptCount")

