package FullTableStatistics

/**
  * Created by HuShiwei on 2016/6/30 0030.
  */
object demo {
  def main(args: Array[String]) {
    val list = List[(String, String)](
      "hello" -> "world",
      "tell me" -> "why"
    )
    println(list.foldLeft("")((x,y)=>x+""+y))
    for (i <- list) {
      println(i._1+" "+i._2)

    }
  }

}
