import boto3

security_group = boto3.client("ec2")

response = security_group.create_security_group(
    Description='Allow HTTP traffiic',
    GroupName='boto-sg',
    VpcId='your_id',
)

print(response['GroupId'])
