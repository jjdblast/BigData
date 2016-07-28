# coding:utf-8
'''
    Created on 2016/7/1 0001 
    @Author:   HuShiwei
'''
'''
ix-esc-ca2-07.ix.netcom.com - - [01/Aug/1995:00:00:12 -0400] "GET /history/apollo/images/apollo-logo1.gif HTTP/1.0" 200 1173
slppp6.intermind.net - - [01/Aug/1995:00:00:13 -0400] "GET /history/apollo/images/apollo-logo.gif HTTP/1.0" 200 3047
uplherc.upl.com - - [01/Aug/1995:00:00:14 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 304 0
133.43.96.45 - - [01/Aug/1995:00:00:16 -0400] "GET /shuttle/missions/sts-69/mission-sts-69.html HTTP/1.0" 200 10566
kgtyk4.kj.yamagata-u.ac.jp - - [01/Aug/1995:00:00:17 -0400] "GET / HTTP/1.0" 200 7280
'''
import datetime
import re

from pyspark.sql import Row

month_map = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
             'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}


def parse_apache_time(s):
    """Convert Apache time format into a Python datetime object
    Args:
        s(str):date and time in Apache time format
    Returns:
        datetime:datetime object (ignore timezone for now)
    """
    return datetime.datetime(int(s[7:11]),
                             month_map[s[3:6]],
                             int(s[0:2]),
                             int(s[12:14]),
                             int(s[15:17]),
                             int(s[18:20]))


def parseApacheLogLine(logline):
    '''Parse a line in the Apache Common Log format
    Args:
        logline(str): a line of text in the apache common log format
    Returns:
        tuple:either a dictionary containing the parts of the apache access log and 1,or the
        original invalid log line and 0
    '''
    match = re.search(APACHE_ACCESS_LOG_PATTERN, logline)
    if match is None:
        return (logline, 0)
    size_field = match.group(9)
    if size_field == '-':
        size = long(0)
    else:
        size = long(match.group(9))
    return (Row(
        host=match.group(1),
        client_identd=match.group(2),
        user_id=match.group(3),
        date_time=match.group(4),
        method=match.group(5),
        endpoint=match.group(6),
        protocol=match.group(7),
        response_code=int(match.group(8)),
        content_size=size
    ), 1)


from pyspark import SparkContext, SparkConf

# baseDir=os.path.join('databricks-datasets')
# inputPath=os.path.join('cs1000','lab2','data-001','apache.access.log.PROGECT')
# logFile=os.path.join(baseDir,inputPath)
logFile = "hdfs://ncp162:8020/hsw/access_log_Aug95"
conf = SparkConf().setAppName("ParseApacheLog")
sc = SparkContext(conf=conf)


def parseLogs():
    '''Read and parse log file'''
    parsed_logs = (sc.textFile(logFile)
                   .map(parseApacheLogLine)
                   .cache())

    access_log = (parsed_logs
                  .filter(lambda s: s[1] == 1)
                  .map(lambda s: s[0])
                  .cache())

    failed_logs = (parsed_logs
                   .filter(lambda s: s[1] == 0)
                   .map(lambda s: s[0]))

    failed_logs_count = failed_logs.count()

    if failed_logs_count > 0:
        print 'Number of invalid logline: %d' % failed_logs.count()
        for line in failed_logs.take(20):
            print 'Invalid logline:%s' % line

    print 'Read %d lines,successfully parsed %d lines,failed to parse %d lines' % (parsed_logs.count(), access_log.count(), failed_logs.count())
    return parsed_logs, access_log, failed_logs


APACHE_ACCESS_LOG_PATTERN = '^(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] "(\S+) (\S+)\s*(\S*)" (\d{3}) (\S+)'

parsed_Logs, access_log, failed_logs = parseLogs()

# Content size statistics
content_sizes=access_log.map(lambda log:log.content_size).cache()
print 'Content Size Avg: %i, Min: %i, Max: %s' %(
    content_sizes.reduce(lambda a,b:a+b)/content_sizes.count(),
    content_sizes.min(),
    content_sizes.max())

#Response Code to Count
responseCodeToCount=access_log.map(lambda log:(log.response_code,1)).reduceByKey(lambda a,b:a+b).cache()
responseCodeToCountList=responseCodeToCount.take(100)
print 'Found %d response codes' % len(responseCodeToCountList)
print 'Response Code Counts: %s' % responseCodeToCountList

import matplotlib.pyplot as plt


