import boto3

ingress = boto3.client("ec2")

response = ingress.authorize_security_group_egress(
    GroupId='sg-0573475846d28fe42',
    IpPermissions=[
        {
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0',
                },
            ],
            'ToPort': 65535,
        },
    ],
)

print(response)

