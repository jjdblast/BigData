package somethingUtils.common;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;

import java.io.InputStream;
import java.util.Iterator;
import java.util.Properties;

/**
 * .properties 文件读取工具类
 * 调用方式：
 * PropertiesUtil.getPropertiesValue("constants.properties","createUrl")
 * @author wangjialing
 * @version 创建时间：2015-10-9 上午11:18:30
 */
public class PropertiesUtil {
	static Log logger = LogFactory.getLog(PropertiesUtil.class);
	static PropertiesUtil p = new PropertiesUtil();
	/**
	 * 读取.properties文件返回值 ;
	 * properties默认存放路径为classpath
	 * @param properties
	 * @param elementName
	 * @return String
	 */
	public static String getPropertiesValue(String properties,String elementName){
		String reValue = "error";
		Properties pro = new Properties();
	    ClassLoader loader = p.getClass().getClassLoader();
		//读取文件
		InputStream in = null;
		try {
			in = loader.getResourceAsStream(properties);
			pro.load(in);
			//取到pro的value值
			Iterator<String> it = pro.stringPropertyNames().iterator();
			while(it.hasNext()){
				String key = it.next();
				if(elementName.equals(key.trim())){
					reValue = pro.getProperty(key);
					break;
				}
			}
			if(in!=null)
				in.close();
		} catch (Exception e) {
			logger.error("读取properties文件错误：",e);
		} 
		return reValue.trim();
	}
}
