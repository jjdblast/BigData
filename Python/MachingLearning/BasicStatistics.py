# coding:utf-8
'''
    Created on 2016/6/22 0022 
    @Author:   HuShiwei
'''
import sys

from pyspark import SparkContext

'''
1|24|M|technician|85711
'''


def convert_year(x):
    try:
        return int(x[-4:])
    except:
        return 1900


if __name__ == '__main__':
    cluster = "local"
    if len(sys.argv) == 2:
        cluster = sys.argv[1]
    sc = SparkContext(cluster, "kmeans")
    user_data = sc.textFile("hdfs://192.168.16.162:8020/hsw/ml-100k/u.user")
    print user_data.first()

    user_fields = user_data.map(lambda line: line.split("|"))
    num_users = user_fields.map(lambda fields: fields[1]).count()
    num_genders = user_fields.map(lambda fields: fields[2]).distinct().count()
    num_occupations = user_fields.map(lambda fields: fields[3]).distinct().count()
    num_zipcodes = user_fields.map(lambda fields: fields[4]).distinct().count()
    print "Users:%d,genders:%d,occupations:%d,ZIP codes:%d" % (num_users, num_genders, num_occupations, num_zipcodes)

    # ages=user_fields.map(lambda x:int(x(1))).collect()

    movie_data = sc.textFile("hdfs://192.168.16.162:8020/hsw/ml-100k/u.item")
    print "u.item first data \n" + movie_data.first()
    '''
    1|Toy Story (1995)|01-Jan-1995||http://us.imdb.com/M/title-exact?Toy%20Story%20(1995)|0|0|0|1|1|1|0|0|0|0|0|0|0|0|0|0|0|0|0
    '''

    movie_fields = movie_data.map(lambda lines: lines.split("|"))
    years = movie_fields.map(lambda fields: fields[2]).map(lambda x: convert_year(x))
    years_filtered = years.filter(lambda x: x != 1900)
    movie_ages = years_filtered.map(lambda yr:  1998 - yr).countByValue()
    values = movie_ages.values()
    print values
    # bins=movie_ages.keys()
    # print bins+"==="+values
    sc.stop()
