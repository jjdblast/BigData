package TxtDataSource

import TxtDataSource.TextFile.TextFileRelation
import org.apache.spark.sql.SQLContext
import org.apache.spark.sql.sources.{BaseRelation, DataSourceRegister, RelationProvider}

/**
  * Created by HuShiwei on 2016/5/27 0027.
  */
class DefaultSource extends RelationProvider with DataSourceRegister{
  override def shortName(): String = "textfile"


  override def createRelation(sqlContext: SQLContext, parameters: Map[String, String]): BaseRelation = {
    TextFileRelation(parameters)(sqlContext)

  }
}
