import boto3

instance = boto3.client("ec2")

response = instance.run_instances(
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/sdh',
            'Ebs': {
                'VolumeSize': 8,
                'VolumeType': 'gp2',
               'DeleteOnTermination': True
            },
        },
    ],
    ImageId="ami-1234567890abcdef",
    KeyName="test",
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1,
    SubnetId='subnet-1234567890abcdef',
    Monitoring={
        'Enabled': True
    },
    Placement={
        'Tenancy': 'default'
    },
    SecurityGroupIds=[
        'sg-1234567890abcdef',
    ],
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'boto-instance',
                },
            ],
        },
    ],
)

print("Creating Instance...")

instance_id = response['Instances'][0]['InstanceId']
print(f'Launched instance {instance_id}')

print("Waiting for Instance to Run")
waiter = instance.get_waiter('instance_running')
waiter.wait(InstanceIds=[instance_id])

print(f'Instance {instance_id} is running')
