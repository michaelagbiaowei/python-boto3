import boto3

keypair = boto3.client("ec2")

response = keypair.create_key_pair(
    KeyName='boto-key',
    KeyType='rsa',
    KeyFormat='pem'
)
print(f'Your key ID is: {response["KeyPairId"]}')