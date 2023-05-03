import boto3

delete = boto3.client("ec2")

response = delete.delete_key_pair(
    KeyName = "boto-key"
)

print(response["RequestId"])