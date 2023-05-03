import boto3

image = boto3.client("ec2")

response = image.create_image(
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/sdh',
            'Ebs': {
                'VolumeSize': 8,
                'VolumeType': 'gp2',
                'DeleteOnTermination': True
            },
        },
        {
            'DeviceName': '/dev/sdc',
            'VirtualName': 'ephemeral1',
        },
    ],
    Description='An AMI for my boto server',
    InstanceId='i-09f2fcce04677c126',
    Name='boto-server',
    NoReboot=True,
    TagSpecifications=[
        {
            'ResourceType': "image",
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'boto-image'
                },
            ]
        },
    ]
)

print(response["ImageId"])