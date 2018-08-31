#!/usr/bin/env python
import boto3,sys, json,os,csv
from pprint import pprint
from datetime import datetime, timedelta
from boto import rds

def get_all_instances(access_key,secret_key,default_region):
	"""
	Method to get all the ec2 instances
	
	"""
	client = boto3.client('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_key,region_name=default_region)

	ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]

	instanceList =[]
	for region in ec2_regions:
		conn = boto3.resource('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_key,
                   region_name=region)
		instances = conn.instances.filter()
		for instance in instances:
			#if instance.state["Name"] == "running":
			instanceList.append({'Name':'InstanceId','Value':instance.id,'region':region})
	
	return instanceList
	
#https://www.highcharts.com/docs/working-with-data/live-data
#Working cloud watch cmd line
#aws cloudwatch get-metric-statistics --namespace AWS/EC2 --metric-name CPUUtilization  --period 3600 \
#--statistics Average --dimensions Name=InstanceId,Value=i-058d282c64b0eb1e7 \
#--start-time 2018-08-28T23:18:00 --end-time 2018-08-29T23:18:00
def get_aws_instance_metrics(access_key,secret_key,default_region,metric_namespace,cpu_metric_name,
dimension_name,instance_id,metric_time_period,metric_statistic,metric_result_unit):
	"""
	Method to get metrics specify - tried to make as generic as possible, to use 
	for both ec2 and rds
	Works for a single instance
	To get average of multiple instances at once, pass a list of dictionaries to
	dimensions
	
	Reference:
	For EC2 - https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ec2-metricscollected.html
	
	For RDS -
	https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Monitoring.html
	"""
	cloudwatch = boto3.client('cloudwatch', aws_access_key_id=access_key, aws_secret_access_key=secret_key,region_name=default_region)
	response = cloudwatch.get_metric_statistics(
		#Namespace='AWS/EC2',
		#MetricName='CPUUtilization',
		Namespace=metric_namespace,        
        MetricName=cpu_metric_name,
        Dimensions=[
			{
			#'Name': 'InstanceId',
			#'Value': 'i-058d282c64b0eb1e7'
			'Name': dimension_name,			
			'Value': instance_id
			}
			],
			StartTime= datetime.today().utcnow() - timedelta(seconds=600),
			EndTime = datetime.today().utcnow(),
			#Period=60, #Every 30 seconds
			Period=metric_time_period,
			Statistics=[
			#'Average',
			metric_statistic,
			],
			#Unit='Percent',
			Unit=metric_result_unit,
			)
	#print(response)
	for cpu in response['Datapoints']:
		if metric_statistic in cpu:
			return cpu[metric_statistic]
			
def print_aws_all_instance_metrics(access_key,secret_key,default_region,		metric_namespace,cpu_metric_name,metric_time_period,metric_statistic,metric_result_unit):
	"""
	Method to get metrics of all instances
	To get average of multiple instances at once, pass a list of dictionaries to
	dimensions
	
	Reference:
	For EC2 - https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ec2-metricscollected.html
	
	For RDS -
	https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Monitoring.html
	
	"""
	outputList = []
	csv_output = []
	all_instances = get_all_instances(access_key,secret_key,default_region)
	instance_id = ''
	metric_output = None
	#print ("{},{}".format('Instance Id','Output'))
	for index in range(len(all_instances)):
			dimension_name = all_instances[index]['Name']
			instance_id = all_instances[index]['Value']
			metric_output = get_aws_instance_metrics(access_key,secret_key,default_region,metric_namespace,cpu_metric_name,dimension_name,instance_id,metric_time_period,metric_statistic,metric_result_unit)
			if metric_output is None:
				csv_output = ("{},{}".format(instance_id,0))
			else:
				csv_output = ("{},{}".format(instance_id,metric_output))
			outputList.append(csv_output)
	return outputList
	
def print_aws_all_db_metrics(access_key,secret_key,default_region,		metric_namespace,cpu_metric_name,metric_time_period,metric_statistic,metric_result_unit):
	"""
	Method to get metrics of all instances
	To get average of multiple instances at once, pass a list of dictionaries to
	dimensions
	
	"""
	outputList = []
	csv_output = []
	all_instances = get_all_db_instances(access_key,secret_key,default_region)
	instance_id = ''
	metric_output = None
	#print ("{},{}".format('Instance Id','Output'))
	for index in range(len(all_instances)):
			dimension_name = all_instances[index]['Name']
			instance_id = all_instances[index]['Value']
			metric_output = get_aws_instance_metrics(access_key,secret_key,default_region,metric_namespace,cpu_metric_name,dimension_name,instance_id,metric_time_period,metric_statistic,metric_result_unit)
			if metric_output is None:
				csv_output = ("{},{}".format(instance_id,0))
			else:
				csv_output = ("{},{}".format(instance_id,metric_output))
			outputList.append(csv_output)
	return outputList
	
def get_all_db_instances(access_key, secret_key,default_region):
	"""
	Method to get all the rds db instances
	
	"""
	dbList = []
	rds = boto3.client('rds', aws_access_key_id=access_key, aws_secret_access_key=secret_key,region_name=default_region)
	try:
	# get all of the db instances
		dbs = rds.describe_db_instances()
		for db in dbs['DBInstances']:
			dbList.append({'Name':'DBInstanceIdentifier','Value':db['DBInstanceIdentifier']})
	except Exception as error:
		print error
	
	return dbList

def print_json_result(result):
	"""
	Method to print the result to json
	
	"""
	print json.dumps(result)

def print_to_csv_file(result,fileName):
	"""
	Method to print the result to json
	
	"""
	
	pwd = os.getcwd()
	outputFileName = pwd+'/'+'output/'+fileName+'.csv'
	os.system("sudo touch "+outputFileName)
	os.system("sudo chmod 777 "+outputFileName)
	f = open(outputFileName,"w+")
	firstLine = "Instance-Id,"+fileName+"\r\n"
	f.write(firstLine)
	for i in result:
		i = i+"\r\n"
		f.write(i)
	f.close()

	
	
	
