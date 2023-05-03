import boto3

reboot = boto3.client("ec2")

response = reboot.reboot_instances(
    InstanceIds=[
        'i-0b8c12d411715d81e',
    ],
)

print(response)
