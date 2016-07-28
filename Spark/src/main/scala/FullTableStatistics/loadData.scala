package FullTableStatistics

import org.apache.spark.sql.SQLContext
import org.apache.spark.{SparkConf, SparkContext}

/**
  * Created by HuShiwei on 2016/6/13 0013.
  */

/** 年龄,工作类型,序号,教育程度,受教育时间,婚姻状况,职业,关系,种族,性别,资本收益,资本损失,每周工作小时数,原籍,收入
  * 39, State-gov, 77516, Bachelors, 13, Never-married, Adm-clerical, Not-in-family, White, Male, 2174, 0, 40, United-States, <=50K
  * 50, Self-emp-not-inc, 83311, Bachelors, 13, Married-civ-spouse, Exec-managerial, Husband, White, Male, 0, 0, 13, United-States, <=50K
  * 38, Private, 215646, HS-grad, 9, Divorced, Handlers-cleaners, Not-in-family, White, Male, 0, 0, 40, United-States, <=50K
  * 53, Private, 234721, 11th, 7, Married-civ-spouse, Handlers-cleaners, Husband, Black, Male, 0, 0, 40, United-States, <=50K
  * 28, Private, 338409, Bachelors, 13, Married-civ-spouse, Prof-specialty, Wife, Black, Female, 0, 0, 40, Cuba, <=50K
  * 37, Private, 284582, Masters, 14, Married-civ-spouse, Exec-managerial, Wife, White, Female, 0, 0, 40, United-States, <=50K
  */
object loadData {
  def main(args: Array[String]) {

    val conf= new SparkConf().setAppName("rowFactory").setMaster("local[*]")
    val sc = new SparkContext(conf)
    val sqlContext = new SQLContext(sc)

    /********************************加载人口普查测试数据集***********************************/
    val textFileDF=sqlContext.read.format("OfflineDataSpark.TxtDataSource").options(Map(
      "sparksql_table_schema"->"(age double, workclass string, fnlwgt string, education string, education_num double, maritial_status string, occupation string, relationship string, race string,sex string, capital_gain string, capital_loss string, hours_per_week double, native_country string, income string)",
      "textfile_path"->"hdfs://ncp162:8020/hsw/FullTableStatistics/adult.data",
      "textfile_table_schema" -> "(0 age double,1 workclass string,2 fnlwgt string,3 education string,4 education_num double,5 maritial_status string,6 occupation string,7 relationship string,8 race string,9 sex string,10 capital_gain string,11 capital_loss string,12 hours_per_week double,13 native_country string,14 income string )"
    )).load()

    textFileDF.show()
    textFileDF.printSchema()

    sc.stop()
  }

}
