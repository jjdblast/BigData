package FullTableStatistics

import org.apache.spark.{SparkConf, SparkContext}

/**
  * Created by HuShiwei on 2016/6/13 0013.
  */
object fullTable {
  def main(args: Array[String]) {
    val path = "hdfs://ncp162:8020/hsw/FullTableStatistics/adult.data"
    val conf = new SparkConf().setAppName("People Info Calculator").setMaster("local[*]")
    val sc = new SparkContext(conf)
    val dataFile = sc.textFile(path, 5)
    dataFile.take(100).foreach(println)
    val MaleRDD=dataFile.filter(lines=> lines.contains("Male"))
    MaleRDD.take(100).foreach(println)
  }

}
