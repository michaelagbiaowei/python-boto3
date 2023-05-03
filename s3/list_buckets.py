import boto3

s3 = boto3.client("s3")

bucket_response = s3.list_buckets()
buckets = bucket_response['Buckets']
print(buckets)