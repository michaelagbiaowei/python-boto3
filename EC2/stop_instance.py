import boto3

stop = boto3.client("ec2")

response = stop.stop_instances(
    InstanceIds=[
        'i-0b8c12d411715d81e',
    ],
    Force=True
)

print(response)