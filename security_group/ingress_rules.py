import boto3

ingress = boto3.client("ec2")

response = ingress.authorize_security_group_ingress(
    GroupId='sg-0573475846d28fe42',
    IpPermissions=[
        {
            'FromPort': 80,
            'IpProtocol': 'tcp',
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0',
                },
            ],
            'ToPort': 80,
        },
    ],
)

print(response)

