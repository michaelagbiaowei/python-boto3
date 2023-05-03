import boto3

ec2 = boto3.resource('ec2')
CreateElasticIp = boto3.client("ec2")
CreateNatGatway = boto3.client("ec2")



vpc = ec2.create_vpc(
    CidrBlock='10.0.0.0/16',
    InstanceTenancy="default",
    TagSpecifications=[
        {
            'ResourceType': "vpc",
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'boto-vpc'
                },
            ]
        },
    ]
)

# # Assign a name to the VPC
# vpc.create_tags(
#     Tags=[
#         {
#             "Key":"Name",
#             "Value":"boto-vpc"
#         }
#     ]
# )

print("Creating VPC...")
vpc.wait_until_available()
print(vpc.id)

# Create and Attach the Internet Gateway
ig = ec2.create_internet_gateway(
    TagSpecifications=[
        {
            'ResourceType': 'internet-gateway',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'boto-ig'
                },
            ]
        },
    ]
)
print("Creating Internet Gateway...")
print(ig.id)
vpc.attach_internet_gateway(InternetGatewayId=ig.id)

# Create a route table and a public route to Internet Gateway
route_table1 = vpc.create_route_table(
    TagSpecifications=[
        {
            'ResourceType': 'route-table',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'boto-route1'
                },
            ]
        },
    ]
)
route1 = route_table1.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=ig.id
)
print("Creating Route Table1...")
print(route_table1.id)

# Create a public Subnet
subnet1 = ec2.create_subnet(
    CidrBlock='10.0.1.0/24', 
    VpcId=vpc.id,
    TagSpecifications=[
        {
            'ResourceType': 'subnet',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'boto-subnet1'
                },
            ]
        },
    ]
)
print("Creating Subnet1...")
print(subnet1.id)

# associate the route table with the subnet
route_table1.associate_with_subnet(SubnetId=subnet1.id)

# Create Elastic IP
elasticIP = CreateElasticIp.allocate_address(
    Domain='vpc',
    TagSpecifications=[
        {
            'ResourceType': 'elastic-ip',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'boto=EIP'
                },
            ]
        },
    ]
)

print({elasticIP["AllocationId"]})
print(f'{elasticIP["PublicIp"]} has been allocated')
# Create a private Subnet
subnet2 = ec2.create_subnet(
    CidrBlock='10.0.2.0/24', 
    VpcId=vpc.id,
    TagSpecifications=[
        {
            'ResourceType': 'subnet',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'boto-subnet2'
                },
            ]
        },
    ]
)
print("Creating Private Subnet...")
print(subnet2.id)

# # Create Nat gateway and Attach the NAT gateway
nat = CreateNatGatway.create_nat_gateway(
    AllocationId=elasticIP["AllocationId"],
    SubnetId=subnet2.id,
    ConnectivityType='public',
    TagSpecifications=[
        {
            'ResourceType': 'natgateway',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'boto-nat'
                },
            ]
        },
    ]
)
print("Creating NAT...")
nat_gateway_id = nat['NatGateway']['NatGatewayId']
waiter = CreateNatGatway.get_waiter('nat_gateway_available')
waiter.wait(NatGatewayIds=[nat_gateway_id])
print(nat_gateway_id)

# Create a route table and a private route to NAT Gateway
route_table2 = vpc.create_route_table(
    TagSpecifications=[
        {
            'ResourceType': 'route-table',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'boto-route2'
                },
            ]
        },
    ]
)
route2 = route_table2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    NatGatewayId=nat_gateway_id
)

print("Creating Route Table2...")
print(route_table2.id)

# associate the route table with the subnet2
route_table2.associate_with_subnet(SubnetId=subnet2.id)

