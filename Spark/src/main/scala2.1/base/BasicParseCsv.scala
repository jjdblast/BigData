/**
 * Illustrates a simple map partition to parse CSV data in Scala
 */
package base

import java.io.{StringReader, StringWriter}

import au.com.bytecode.opencsv.{CSVReader, CSVWriter}
import org.apache.spark._

import scala.collection.JavaConversions._

object BasicParseCsv {
  case class Person(name: String, favouriteAnimal: String)

  def main(args: Array[String]) {
    if (args.length < 3) {
      println("Usage: [sparkmaster] [inputfile] [outputfile]")
      exit(1)
    }
    val master = args(0)
    val inputFile = args(1)
    val outputFile = args(2)
    val sc = new SparkContext(master, "BasicParseCsv", System.getenv("SPARK_HOME"))
    val input = sc.textFile(inputFile)
    val result = input.map{ line =>
      val reader = new CSVReader(new StringReader(line));
      reader.readNext();
    }
    val people = result.map(x => Person(x(0), x(1)))
    val pandaLovers = people.filter(person => person.favouriteAnimal == "panda")
    pandaLovers.map(person => List(person.name, person.favouriteAnimal).toArray).mapPartitions{people =>
      val stringWriter = new StringWriter();
      val csvWriter = new CSVWriter(stringWriter);
      csvWriter.writeAll(people.toList)
      Iterator(stringWriter.toString)
    }.saveAsTextFile(outputFile)
  }
}
