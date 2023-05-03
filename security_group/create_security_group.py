import boto3

security_group = boto3.client("ec2")

response = security_group.create_security_group(
    Description='Allow HTTP traffiic',
    GroupName='boto-sg',
    VpcId='vpc-0b213113ae9f7eef3',
)

print(response['GroupId'])