package TxtDataSource

import java.util.Properties

import org.apache.spark.sql.SQLContext
import org.apache.spark.{SparkConf, SparkContext}

/**
  * Created by HuShiwei on 2016/5/29 0029.
  */
object readTextFile {
  def main(args: Array[String]) {
    val conf= new SparkConf().setAppName("rowFactory").setMaster("local[*]")
    val sc = new SparkContext(conf)
    val sqlContext = new SQLContext(sc)
//    OfflineDataSpark.TxtDataSource
//    textfile
/*    val textFileDF=sqlContext.read.format("OfflineDataSpark.TxtDataSource").options(Map(
      "sparksql_table_schema"->"(id int, name string, area string, address string, code string)",
      "textfile_path"->"hdfs://192.168.4.202:8020/examples/clean/custom1.txt",
      "textfile_table_schema" -> "(0 id int, 1 name string, 2 area string, 3 address string, 4 code string )"
    )).load()*/

    val textFileDF=sqlContext.read.format("OfflineDataSpark.TxtDataSource").options(Map(
      "sparksql_table_schema"->"(num1 string, num2 string, num3 string)",
      "textfile_path"->"hdfs://ncp162:8020/hsw/testSet.txt",
      "textfile_table_schema" -> "(0 num1 string, 1 num2 string, 2 num3 string)"
    )).load()



/*    val textFileDF=sqlContext.read.format("OfflineDataSpark.TxtDataSource").options(Map(
      "sparksql_table_schema"->"(id int, name string, area string,  code string)",
      "textfile_path"->"hdfs://192.168.0.131:9000/hsw/Custom1.txt",
      "textfile_table_schema" -> "(0 id int, 1 name string, 2 area string,4 code string )"
    )).load()*/



    textFileDF.show()

    val prop = new Properties()
    prop.put("driver", "com.mysql.jdbc.Driver")
    prop.put("user", "root")
    prop.put("password", "5Rb!!@bqC%")
    textFileDF.write.mode("overwrite").jdbc(
      "jdbc:mysql://192.168.4.213:3306/sparkSQL",
      "pythonModel",
      prop
    )

    textFileDF.printSchema()
  }

}
