package FullTableStatistics

import org.apache.spark.sql.SQLContext
import org.apache.spark.{SparkConf, SparkContext}
import com.databricks.spark.csv._
/**
  * Created by HuShiwei on 2016/6/13 0013.
  */
object tableStatistics {
  def main(args: Array[String]) {
    val conf = new SparkConf().setAppName("full table statics").setMaster("local[*]")
    val sc = new SparkContext(conf)
    val sqlContext = new SQLContext(sc)
        val dataRDD = sqlContext.read.format("csv").load("hdfs://ncp162:8020/hsw/FullTableStatistics/AirQualityUCI.csv")
//    val path = "hdfs://ncp162:8020/hsw/FullTableStatistics/AirQualityUCI.csv"
//    val dataRDD=sqlContext.csvFile(path)

    dataRDD.show()
    sc.stop()
  }

}
