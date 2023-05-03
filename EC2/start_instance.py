import boto3

start = boto3.client("ec2")

response = start.start_instances(
    InstanceIds=[
        'i-0b8c12d411715d81e',
    ]
)

print(response)
