package FullTableStatistics

import org.apache.spark.sql.SQLContext
import org.apache.spark.{SparkConf, SparkContext}

/**
  * Created by HuShiwei on 2016/6/29 0029.
  */

/**
  * root
  * |-- ListSector: string (nullable = true)
  * |-- closePrice: double (nullable = true)
  * |-- dealAmount: long (nullable = true)
  * |-- exchangeCD: string (nullable = true)
  * |-- highestPrice: double (nullable = true)
  * |-- isOpen: long (nullable = true)
  * |-- listDate: string (nullable = true)
  * |-- lowestPrice: double (nullable = true)
  * |-- marketValue: double (nullable = true)
  * |-- negMarketValue: double (nullable = true)
  * |-- openPrice: double (nullable = true)
  * |-- preClosePrice: double (nullable = true)
  * |-- secID: string (nullable = true)
  * |-- secShortName: string (nullable = true)
  * |-- ticker: string (nullable = true)
  * |-- totalShares: long (nullable = true)
  * |-- tradeDate: string (nullable = true)
  * |-- turnoverValue: double (nullable = true)
  */
object FullTableStatistics {
  def main(args: Array[String]) {
    val path = "hdfs://ncp162:8020/hsw/FullTableStatistics/stock_5.json"
    val conf = new SparkConf().setAppName("People Info Calculator").setMaster("local[*]")
    val sc = new SparkContext(conf)
    val sqlContext = new SQLContext(sc)
    val jsonRDD = sqlContext.read.json(path)
    //    jsonRDD.printSchema()
    jsonRDD.show()
    jsonRDD.describe().show()

    jsonRDD.select("closePrice", "highestPrice", "lowestPrice").describe().show()
    jsonRDD

    sc.stop()
  }
}
