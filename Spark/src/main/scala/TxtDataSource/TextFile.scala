package TxtDataSource

import org.apache.spark.rdd.RDD
import org.apache.spark.sql.sources.{BaseRelation, TableScan}
import org.apache.spark.sql.types._
import org.apache.spark.sql.{Row, SQLContext}

import scala.collection.mutable.ArrayBuffer

/**
  * Created by HuShiwei on 2016/5/27 0027.
  */
object TextFile extends Serializable {

  /*
    val textFileDDL =
      s"""
         |CREATE TEMPORARY TABLE textFileTable
         |USING OfflineDataSpark.TxtDataSource
         |OPTIONS (
         | textFile
       """.stripMargin*/

  /**
    * "sparksql_table_schema" -> "(id int, name string, area string, address string, code string)",
    * "textfile_path" -> "hdfs://Jusfoun2016/clean/custom1.txt",
    * "textfile_table_schema" -> "(0 id int, 1 name string, 2 area string, 3 address string, 4 code string )"
    */


  case class TextFileRelation(@transient val textProps: Map[String, String])(@transient val sqlContext: SQLContext) extends BaseRelation with Serializable with TableScan {
    val registerTableSchema = textProps.getOrElse("sparksql_table_schema", sys.error("not valid schema"))
    val textfilePath = textProps.getOrElse("textfile_path", sys.error("not valid schema"))
    val textfileTableSchema = textProps.getOrElse("textfile_table_schema", sys.error("not valid schema"))


    val registerTableFields = extractRegisterSchema(registerTableSchema)
    val textFileTableFields = extractTextFileSchema(textfileTableSchema)

    //    registerTableSchema (id int, name string, area string, address string, code string)
    def extractRegisterSchema(registerTableSchema: String): Array[RegisterSchemaField] = {
      val fieldsStr = registerTableSchema.trim.drop(1).dropRight(1)
      val fieldsArray = fieldsStr.split(",").map(_.trim)
      fieldsArray.map { fieldString =>
        val fieldArr = fieldString.split(" ")
        val fieldname = fieldArr(0)
        val fieldType = fieldArr(1)
        RegisterSchemaField(fieldname, fieldType)
      }
    }

    //    textfileTableSchema (0 id int, 1 name string, 2 area string, 3 address string, 4 code string )
    def extractTextFileSchema(textfileTableSchema: String): Array[TextFileSchemaField] = {
      val fieldsStr = textfileTableSchema.trim.drop(1).dropRight(1)
      val fieldsArray = fieldsStr.split(",").map(_.trim)
      fieldsArray.map { fieldString =>
        val fieldArr = fieldString.split(" ")
        val index = fieldArr(0).toInt
        val fieldname = fieldArr(1)
        val fieldType = fieldArr(2)
        TextFileSchemaField(index, fieldname, fieldType)
      }
    }

    lazy val schema: StructType = {
      val fields = registerTableFields.map { field =>
        val name = field.fieldName
        val relatedType = field.fieldType match {
          case "string" =>
            SchemaType(StringType, nullable = false)
          case "int" =>
            SchemaType(IntegerType, nullable = false)
          case "long" =>
            SchemaType(LongType, nullable = false)
          case "double" =>
            SchemaType(DoubleType, nullable = false)
        }
        StructField(name, relatedType.dataType, relatedType.nullable)

      }
      StructType(fields)
    }
    /**
      * 100, John Smith, Austin, TX, 78727
      * 200, Joe Johnson, Dallas, TX, 75201
      * 300, Bob Jones, Houston, TX, 77028
      * 400, Andy Davis, San Antonio, TX, 78227
      * 500, James Williams, Austin, TX, 78727
      */
    lazy val buildScan: RDD[Row] = {
      val textFileRDD = sqlContext.sparkContext.textFile(textfilePath)
      val rs = textFileRDD.map(_.split("\t")).map(fieldsArr => {
        var values = new ArrayBuffer[Any]()
        textFileTableFields.foreach { field =>
          val index = field.index
          val fieldname = field.fieldName
          val filedtype = field.fieldType
          filedtype match {
            case "string" =>
              values += fieldsArr(index).toString
            case "int" =>
              values += fieldsArr(index).toInt
            case "long" =>
              values += fieldsArr(index).toLong
            case "double" =>
              values += fieldsArr(index).toDouble
          }
        }
        Row.fromSeq(values.toSeq)
      })
      rs
    }

    private case class SchemaType(dataType: DataType, nullable: Boolean)

  }

}
