import boto3

ec2 = boto3.resource('ec2')
DeleteNatGatway = boto3.client("ec2")
DeleteElasticIp = boto3.client("ec2")

# Delete nat
DeleteNat = DeleteNatGatway.delete_nat_gateway(NatGatewayId='nat-083132f427b06517d')

# # Detach Elatic IP
DetachEIP = DeleteElasticIp.disassociate_address(
    AssociationId='your_id',
    PublicIp='your_elastic_ip',
)

# # Detach and Delete  igw
DetachIgw = ec2.detach_internet_gateway(
    InternetGatewayId='your_id',
    VpcId='vpc-0157aaad35705accc'
)
DeleteIgw = ec2.delete_internet_gateway(
    InternetGatewayId='your_id',
    VpcId='vpc-0157aaad35705accc'
)

# # Delete Route tables
DeletRouteTable1 = ec2.delete_route_table(
    RouteTableId='your_id'
)
DeletRouteTable2 = ec2.delete_route_table(
    RouteTableId='your_id'
)

# # Delete Subnets
DeleteSubnet1 = ec2.delete_subnet(
    SubnetId='string',
)
DeleteSubnet2 = ec2.delete_subnet(
    SubnetId='string',
)