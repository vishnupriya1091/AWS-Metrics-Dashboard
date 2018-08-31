import unittest
import boto3
import aws_lib_functions

# can be retrieved from a separate file - but using as global variables for now
access_key = "AKIAJVUGDZPQOZTV5M6Q"
secret_key = "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"
default_region = "us-east-2"

class BasicConnectionTest(unittest.TestCase):
"""

Unit Test to avoid null values

"""
    def test_connection(self):
        client = boto3.client('ec2')
        self.assertIsNotNone(client)

    def test_aws_lib_functions(self):
        self.assertIsNotNone(aws_lib_functions.get_all_instances(access_key,secret_key,default_region))

    def test_cpu_utilization(self):
		metric_namespace = 'AWS/EC2'
		cpu_metric_name = 'CPUUtilization'
		dimension_name = 'InstanceId'
		instance_id = 'i-058d282c64b0eb1e7'
		metric_time_period = 60
		metric_statistic = 'Average'
		metric_result_unit = 'Percent'
		self.assertIsNotNone(aws_lib_functions.get_aws_instance_metrics(access_key,secret_key,default_region,metric_namespace,cpu_metric_name,			dimension_name,instance_id,metric_time_period,metric_statistic,metric_result_unit))

    def test_rds_instance(self):
        self.assertIsNotNone(aws_lib_functions.get_all_db_instances(access_key, secret_key,default_region))
	
	def test_db_utilization(self):
		metric_namespace = 'AWS/RDS'
		cpu_metric_name = 'CPUUtilization'
		dimension_name = 'DBInstanceIdentifier'
		instance_id = 'tutorial-db-instance'
		metric_time_period = 3600
		metric_statistic = 'Average'
		metric_result_unit = 'Percent'
		self.assertIsNotNone(aws_lib_functions.get_aws_instance_metrics(access_key,secret_key,default_region,metric_namespace,cpu_metric_name,			dimension_name,instance_id,metric_time_period,metric_statistic,metric_result_unit))



if __name__ == '__main__':
    unittest.main()


# aws_metrics_unit_tests.py