package somethingUtils.model;

import java.io.Serializable;

public class AlertMessage implements Serializable {

	private static final long serialVersionUID = 1L;

	private String jobId;// 工作流jobId
	private String nodeId;// 工作流nodeId
	private String alertId;// 报警配置Id，如果是系统报警，此项可为null
	private String suggest;// 处理建议
	private String method;// 报错方法全路径。如com.test.test();
	private String message;// 报警信息，或者异常信息。

	public String getJobId() {
		return jobId;
	}

	public void setJobId(String jobId) {
		this.jobId = jobId;
	}

	public String getNodeId() {
		return nodeId;
	}

	public void setNodeId(String nodeId) {
		this.nodeId = nodeId;
	}

	public String getAlertId() {
		return alertId;
	}

	public void setAlertId(String alertId) {
		this.alertId = alertId;
	}

	public String getSuggest() {
		return suggest;
	}

	public void setSuggest(String suggest) {
		this.suggest = suggest;
	}

	public String getMethod() {
		return method;
	}

	public void setMethod(String method) {
		this.method = method;
	}
	public String getMessage() {
		return message;
	}

	public void setMessage(String message) {
		this.message = message;
	}
	


}
