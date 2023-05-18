<img align="center" alt="Coding" src="https://directdevops.blog/wp-content/uploads/2019/03/boto3.jpeg">

Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK) for Python, which allows Python developers to write software that makes use of services like Amazon S3 and Amazon EC2.

This guide details the steps needed to install or update the AWS SDK for Python

## **Requirements to install Boto3**

Before installing Boto3, install Python 3.7 or higher

## **Install Boto3**

Install the latest Boto3 release via pip:

    pip install boto3

If your project requires a specific version of Boto3, or has compatibility concerns with certain versions, you may provide constraints when installing:

    # Install Boto3 version 1.0 specifically
    pip install boto3==1.0.0

    # Make sure Boto3 is no older than version 1.15.0
    pip install boto3>=1.15.0

    # Avoid versions of Boto3 newer than version 1.15.3
    pip install boto3<=1.15.3

## **Configuration**

Before using Boto3, you need to set up authentication credentials for your AWS account using either the <a href="https://console.aws.amazon.com/iam/home"><b>IAM Console</b></a> for all of my projects**or the AWS CLI. You can either choose an existing user or create a new one.

For instructions about how to create a user using the IAM Console, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console"><b>Creating IAM users.</b></a> Once the user has been created, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey"><b>Managing access keys</b></a> to learn how to create and retrieve the keys used to authenticate the user.

If you have the <a href="http://aws.amazon.com/cli/"><b>AWS CLI</b></a> installed, then you can use the aws configure command to configure your credentials file:

    aws configure

Alternatively, you can create the credentials file yourself. By default, its location is ~/.aws/credentials. At a minimum, the credentials file should specify the access key and secret access key. In this example, the key and secret key for the account are specified in the default profile:

    [default]
    aws_access_key_id = YOUR_ACCESS_KEY
    aws_secret_access_key = YOUR_SECRET_KEY

You may also want to add a default region to the AWS configuration file, which is located by default at `~/.aws/config:`

    [default]

    region=us-east-1
    output = json

Alternatively, you can pass a region_name when creating clients and resources.

You have now configured credentials for the default profile as well as a default region to use when creating connections. See Configuration for in-depth configuration sources and options.

## **Using Boto3**

To use Boto3, create a .py Script and import boto3 indicating which service or services you’re going to use:

    import boto3

    # Create an ec2 client
    client = boto3.client('ec2')

Now that you have an ec2 client, you can make send requests to the service.

Use the `run_instances()` method to create an instance:

    response = client.run_instances(
        ImageId='ami-1234567890abcdef',
        InstanceType='t2.micro',
        KeyName='my-key-pair',
        MinCount=1,
        MaxCount=1
    )

    print(response)

You can replace the values of `ImageId`, `InstanceType`, and `KeyName` with your own values.

Now, you are all set to create an instance, execute the script from a terminal (CLI) with the following command.

    python your-script.py

## **Credits**

<a href="https://boto3.amazonaws.com/v1/documentation/api/latest/index.html"><b>Boto3 1.26.129 documentation - Amazon Web Services</b></a>



