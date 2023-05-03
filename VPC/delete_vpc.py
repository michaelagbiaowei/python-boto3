import boto3

import boto3

ec2 = boto3.resource('ec2')
vpc = ec2.Vpc('vpc-0ad2289b8e0a7c4b6')
vpc.delete()