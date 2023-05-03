import boto3

delete = boto3.client("ec2")

response = delete.delete_security_group(
    GroupName='boto-sg',
)

print(response["RequestId"])