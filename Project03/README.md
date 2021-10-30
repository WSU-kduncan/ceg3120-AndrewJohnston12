## Andrew Johnston Project03 

## Creating a VPC 
Creating the VPC was really straight forward and the first step was like buliding the walls of your 
house just making sure that you can add the subnet and internet gateway and etc to the same VPC

## Creating a Subnet
the subnet is a range of IP addresses in you VPC. and after you create your subnet you specify the IPv4 
CIDR block for the subnet , which is a subset of the VPC CIDR block. when you create a VPC, you must 
specify a range of IPv4 addresses for the VPC in the form of a CIDR block.

## Creating a Internet Gateway
its in the name but a Internet Gateway enables internet access to the VPC. You can add Public and private 
subnets so you can specify a route for the internet gateway to all destinations not explicitly known to 
the route table.

## Creating a route table 
when you use a route tables you use it to control where network traffic is directed. Each subnet in your 
VPC must be associated with a route table, which controls the routing for the subnet.
You can explicitly associate a subnet with a particular route table.

## Creating a security group
the security group can make rules for the outbound and inbound of ip addresses and with AWS you can add 
certain ip addresses such as your home IP and Places like Wright State 

