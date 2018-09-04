from aws_lib_functions import *
from get_keys import *

access_key = get_keys()['key']
secret_key = get_keys()['value']
default_region = get_keys()['region']

def get_user_operation(userFuncName):
	try:
		# get the instances of ec2
		# all the cpu metric names and units are based on aws documentation
		if userFuncName=='getInstances':
			res = get_all_instances(access_key,secret_key,default_region)
			print_json_result(res)
			
		# get the instances of db - rds instance
		elif userFuncName=='getDBInstances':
			res = get_all_db_instances(access_key,secret_key,default_region)
			print_json_result(res)
			
		# get the metrics for a single specified ec2 instance	
		elif userFuncName=='getMetrics':
			metric_namespace = 'AWS/EC2'
			cpu_metric_name = 'CPUUtilization'
			dimension_name = 'InstanceId'
			instance_id = 'i-058d282c64b0eb1e7'
			metric_time_period = 60
			metric_statistic = 'Average'
			metric_result_unit = 'Percent'
			# one generic method use to fetch metrics for all types of instances
			res = get_aws_instance_metrics(access_key,secret_key,default_region,metric_namespace,cpu_metric_name,
			dimension_name,instance_id,metric_time_period,
			metric_statistic,metric_result_unit)
			print_json_result(res)
		
		# get the metrics for a single specified db instance	
		elif userFuncName=='getDBMetrics':
			metric_namespace = 'AWS/RDS'
			cpu_metric_name = 'CPUUtilization'
			dimension_name = 'DBInstanceIdentifier'
			instance_id = 'tutorial-db-instance'
			metric_time_period = 3600
			metric_statistic = 'Average'
			metric_result_unit = 'Percent'
			res = get_aws_instance_metrics(access_key,secret_key,default_region,metric_namespace,cpu_metric_name,
			dimension_name,instance_id,metric_time_period,
			metric_statistic,metric_result_unit)
			print_json_result(res)
		
		# get cpu utilization for all ec2 instances
		elif userFuncName=='AllInstanceNetworkIn':
			metric_namespace = 'AWS/EC2'
			cpu_metric_name = 'NetworkIn'
			metric_time_period = 360000
			metric_statistic = 'Average'
			metric_result_unit = 'Bytes'
			outputList = print_aws_all_instance_metrics(access_key,secret_key,default_region,metric_namespace,cpu_metric_name,metric_time_period,metric_statistic,metric_result_unit)
			fileName = userFuncName
			print_to_csv_file(outputList,fileName)
			print_json_result('CSVFileCreated')
			
		# get cpu utilization for all ec2 instances
		elif userFuncName=='AllInstanceCPUUsage':
			metric_namespace = 'AWS/EC2'
			cpu_metric_name = 'CPUUtilization'
			metric_time_period = 60
			metric_statistic = 'Average'
			metric_result_unit = 'Percent'
			outputList = print_aws_all_instance_metrics(access_key,secret_key,default_region,metric_namespace,cpu_metric_name,metric_time_period,metric_statistic,metric_result_unit)
			fileName = userFuncName
			print_to_csv_file(outputList,fileName)
			print_json_result('CSVFileCreated')
			
		# get db read latency for all ec2 instances	
		elif userFuncName=='AllInstanceNetworkPacketsIn':
			metric_namespace = 'AWS/EC2'
			cpu_metric_name = 'NetworkPacketsIn'
			metric_time_period = 6
			metric_statistic = 'Average'
			metric_result_unit = 'Count'
			outputList = print_aws_all_instance_metrics(access_key,secret_key,default_region,metric_namespace,cpu_metric_name,metric_time_period,metric_statistic,metric_result_unit)
			fileName = userFuncName 
			print_to_csv_file(outputList,fileName)
			print_json_result('CSVFileCreated')
		
		# get cpu utilization for all rds db instances	
		elif userFuncName=='AllInstanceDBUsage':
			metric_namespace = 'AWS/RDS'
			cpu_metric_name = 'CPUUtilization'
			metric_time_period = 3600
			metric_statistic = 'Average'
			metric_result_unit = 'Percent'
			outputList = print_aws_all_db_metrics(access_key,secret_key,default_region,metric_namespace,cpu_metric_name,metric_time_period,metric_statistic,metric_result_unit)
			fileName = userFuncName 
			print_to_csv_file(outputList,fileName)
			print_json_result('CSVFileCreated')
			
					
		# get db read throughput for all rds db instances	
		elif userFuncName=='AllInstanceDBReadThroughput':
			metric_namespace = 'AWS/RDS'
			cpu_metric_name = 'ReadThroughput'
			metric_time_period = 3600
			metric_statistic = 'Average'
			metric_result_unit = 'Bytes/Second'
			outputList = print_aws_all_db_metrics(access_key,secret_key,default_region,metric_namespace,cpu_metric_name,metric_time_period,metric_statistic,metric_result_unit)
			fileName = userFuncName 
			print_to_csv_file(outputList,fileName)
			print_json_result('CSVFileCreated')
			
		# get db write throughput for all rds db instances	
		elif userFuncName=='AllInstanceDBWriteThroughput':
			metric_namespace = 'AWS/RDS'
			cpu_metric_name = 'WriteThroughput'
			metric_time_period = 60
			metric_statistic = 'Average'
			metric_result_unit = 'Bytes/Second'
			outputList = print_aws_all_db_metrics(access_key,secret_key,default_region,metric_namespace,cpu_metric_name,metric_time_period,metric_statistic,metric_result_unit)
			fileName = userFuncName 
			print_to_csv_file(outputList,fileName)
			print_json_result('CSVFileCreated')
		else:
			raise Exception('Not found')
		
	except Exception as e:
		print "Error in fetching user request : "+str(e)
		sys.exit(1)
			

funcName = sys.argv[1].strip()
get_user_operation(funcName)