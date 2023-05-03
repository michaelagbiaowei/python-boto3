import boto3

terminate = boto3.client("ec2")

response = terminate.terminate_instances(
    InstanceIds=[
        'i-0b8c12d411715d81e',
    ],
    DryRun=False
)

print(response)