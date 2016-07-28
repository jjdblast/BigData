import TxtDataSource.TextFile.TextFileRelation
import org.apache.spark.sql.SQLContext

import scala.collection.immutable.HashMap

/**
  * Created by HuShiwei on 2016/5/28 0028.
  */
package object TxtDataSource {

  abstract class SchemaField extends Serializable

  case class RegisterSchemaField(fieldName: String, fieldType: String) extends SchemaField with Serializable

  case class TextFileSchemaField(index: Int, fieldName: String, fieldType: String) extends SchemaField with Serializable

  case class Parameter(name: String)

  protected val SPARK_SQL_TABLE_SCHEMA = Parameter("sparksql_table_schema")
  protected val TEXTFILE_PATH = Parameter("textfile_path")
  protected val TEXTFILE_TABLE_SCHEMA = Parameter("textfile_table_schema")

  implicit class TextFileContext(sqlContext: SQLContext) {
    def TextFileTable(sparksqlTableSchema: String, textfilePath: String, textfileTableSchema: String) = {
      var params = new HashMap[String, String]
      params += (SPARK_SQL_TABLE_SCHEMA.name -> sparksqlTableSchema)
      params += (TEXTFILE_PATH.name -> textfilePath)
      params += (TEXTFILE_TABLE_SCHEMA.name -> textfileTableSchema)
      sqlContext.baseRelationToDataFrame(TextFileRelation(params)(sqlContext))
    }
  }

}
