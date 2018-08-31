# AWS-Metrics-Dashboard
AWS Metrics Dashboard is a web application to display the AWS Metrics of EC2 and RDS Instances.
It is developed using Python(boto3) API, PHP and HTML/CSS/JS(jQuery).
The results are visualized using HighCharts JS.

URL of the application - http://52.15.80.38/view.html

The output folder consists of all the csv files generated based on the user click.
pyscripts folder  - has the backend python code to fetch the instance results using boto3 api.
API - Use http://52.15.80.38/index.php?display=(:text of the parameter in the web page)

Command line usage for python -
python get_user_request.py <user_request>
Example : python get_user_request.py AllInstanceNetworkIn


Unit Tests:
pyscripts folder has aws_metrics_unit_tests.py that checks if the instances are being returned or not.
Command line usage for unit tests python:
python aws_metrics_unit_tests.py
