package LogProcess

import org.apache.spark.sql.SQLContext
import org.apache.spark.{SparkConf, SparkContext}
/**
  * Created by HuShiwei on 2016/5/18.
  */
object readLog {
  def main(args: Array[String]) {
    val conf=new SparkConf().setAppName("spark-load-log").setMaster("local[5]")
    val sc=new SparkContext(conf)
    val sqlContext=new SQLContext(sc)
    val textRDD = sc.textFile("hdfs://ubt202:8020/examples/logprocess/access_log",5)
//    sc.newAPIHadoopFile()
    textRDD.cache()
//    显示日志的总行数
    val lines=textRDD.count()
    println(lines)

    //    统计每个IP的访问次数,排序显示
    val count=textRDD.map(_.split(" ")).map(x => (x(0),1)).reduceByKey(_+_).map{x =>(x._2 , x._1)}.sortByKey(true).map(y => (y._2 , y._1))
      count.foreach(a=>println("访问ip: "+a._1+" 的访问次数: "+a._2))

//    404




  }


}
