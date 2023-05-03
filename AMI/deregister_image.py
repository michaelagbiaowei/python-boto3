import boto3

delete =  boto3.client("ec2")

response = delete.deregister_image(
    ImageId="ami-066d59f8b1513749d"
)

print(response)